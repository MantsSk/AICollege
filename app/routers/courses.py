from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.deps import current_user_optional, require_user
from app.models import ChatConversation, Course, Lesson, User
from app.services import (
    ai_messages_remaining,
    can_access_lesson,
    completed_lesson_ids,
    course_progress,
    lesson_index,
    mark_lesson_complete,
)
from app.templating import is_htmx, templates

router = APIRouter()


@router.get("/courses", response_class=HTMLResponse)
def catalog(request: Request, db: Session = Depends(get_db), user=Depends(current_user_optional)):
    courses = db.scalars(select(Course).order_by(Course.order)).all()
    cards = []
    for course in courses:
        done, total, percent = course_progress(db, user, course)
        cards.append({"course": course, "done": done, "total": total, "percent": percent})
    return templates.TemplateResponse(
        request,
        "catalog.html",
        {"request": request, "user": user, "cards": cards},
    )


@router.get("/courses/{course_slug}", response_class=HTMLResponse)
def course_detail(
    course_slug: str,
    request: Request,
    db: Session = Depends(get_db),
    user=Depends(current_user_optional),
):
    course = db.scalar(select(Course).where(Course.slug == course_slug))
    if course is None:
        return templates.TemplateResponse(
            request, "errors/404.html", {"request": request, "user": user}, status_code=404
        )
    done_ids = completed_lesson_ids(db, user) if user else set()
    done, total, percent = course_progress(db, user, course)
    lessons = []
    for lesson in course.lessons:
        lessons.append(
            {
                "lesson": lesson,
                "accessible": can_access_lesson(user, lesson, course),
                "completed": lesson.id in done_ids,
                "index": lesson_index(lesson, course),
            }
        )
    return templates.TemplateResponse(
        request,
        "course_detail.html",
        {
            "request": request,
            "user": user,
            "course": course,
            "lessons": lessons,
            "done": done,
            "total": total,
            "percent": percent,
        },
    )


def _load_lesson(db: Session, course_slug: str, lesson_slug: str):
    course = db.scalar(select(Course).where(Course.slug == course_slug))
    if course is None:
        return None, None
    lesson = db.scalar(
        select(Lesson).where(Lesson.course_id == course.id, Lesson.slug == lesson_slug)
    )
    return course, lesson


@router.get("/courses/{course_slug}/{lesson_slug}", response_class=HTMLResponse)
def lesson_page(
    course_slug: str,
    lesson_slug: str,
    request: Request,
    db: Session = Depends(get_db),
    user=Depends(current_user_optional),
):
    course, lesson = _load_lesson(db, course_slug, lesson_slug)
    if course is None or lesson is None:
        return templates.TemplateResponse(
            request, "errors/404.html", {"request": request, "user": user}, status_code=404
        )

    if not can_access_lesson(user, lesson, course):
        return templates.TemplateResponse(
            request,
            "lesson_locked.html",
            {"request": request, "user": user, "course": course, "lesson": lesson},
            status_code=403,
        )

    idx = lesson_index(lesson, course)
    lessons = course.lessons
    prev_lesson = lessons[idx - 1] if idx > 0 else None
    next_lesson = lessons[idx + 1] if idx < len(lessons) - 1 else None

    done_ids = completed_lesson_ids(db, user) if user else set()
    done, total, percent = course_progress(db, user, course)

    mentor_history: list[dict] = []
    mentor_remaining = 0
    if user:
        mentor_remaining = ai_messages_remaining(db, user)
        convo = db.scalar(
            select(ChatConversation).where(
                ChatConversation.user_id == user.id,
                ChatConversation.lesson_id == lesson.id,
            )
        )
        if convo:
            mentor_history = [
                {"role": m.role, "content": m.content} for m in convo.messages
            ]

    return templates.TemplateResponse(
        request,
        "lesson.html",
        {
            "request": request,
            "user": user,
            "course": course,
            "lesson": lesson,
            "prev_lesson": prev_lesson,
            "next_lesson": next_lesson,
            "completed": lesson.id in done_ids,
            "lesson_number": idx + 1,
            "lesson_total": len(lessons),
            "progress_percent": percent,
            "progress_done": done,
            "progress_total": total,
            "mentor_history": mentor_history,
            "mentor_remaining": mentor_remaining,
        },
    )


@router.post("/courses/{course_slug}/{lesson_slug}/complete", response_class=HTMLResponse)
def complete_lesson(
    course_slug: str,
    lesson_slug: str,
    request: Request,
    db: Session = Depends(get_db),
    user: User = Depends(require_user),
):
    course, lesson = _load_lesson(db, course_slug, lesson_slug)
    if course is None or lesson is None:
        return HTMLResponse("Not found", status_code=404)

    mark_lesson_complete(db, user, lesson)
    done, total, percent = course_progress(db, user, course)

    # HTMX returns just the updated progress + completed button fragment.
    return templates.TemplateResponse(
        request,
        "partials/lesson_complete.html",
        {
            "request": request,
            "user": user,
            "course": course,
            "lesson": lesson,
            "progress_percent": percent,
            "progress_done": done,
            "progress_total": total,
            "completed": True,
        },
    )
