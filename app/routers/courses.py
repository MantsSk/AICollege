import random

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.course_paths import PUBLISHED_COURSE_SLUGS, is_published_course
from app.activities import get_activities
from app.database import get_db
from app.deps import current_user_optional, require_user
from app.course_i18n import localize_course
from app.i18n import get_language
from app.models import ChatConversation, Course, Lesson, User
from app.quizzes import course_questions, get_quiz
from app.services import (
    ai_messages_remaining,
    can_access_lesson,
    completed_lesson_ids,
    course_progress,
    get_quiz_result,
    lesson_index,
    mark_lesson_complete,
    save_quiz_result,
)
from app.templating import is_htmx, templates

router = APIRouter()


@router.get("/courses", response_class=HTMLResponse)
def catalog(request: Request, db: Session = Depends(get_db), user=Depends(current_user_optional)):
    courses = db.scalars(
        select(Course)
        .where(Course.slug.in_(PUBLISHED_COURSE_SLUGS))
        .order_by(Course.order)
    ).all()
    lang = get_language(request)
    cards = []
    for course in courses:
        done, total, percent = course_progress(db, user, course)
        cards.append({"course": localize_course(course, lang), "done": done, "total": total, "percent": percent})
    return templates.TemplateResponse(
        request,
        "catalog.html",
        {
            "request": request,
            "user": user,
            "cards": cards,
        },
    )


@router.get("/challenges", response_class=HTMLResponse)
def challenges(
    request: Request,
    db: Session = Depends(get_db),
    user=Depends(current_user_optional),
):
    """A practice catalog assembled from each course's existing quiz bank."""
    courses = db.scalars(
        select(Course)
        .where(Course.slug.in_(PUBLISHED_COURSE_SLUGS))
        .order_by(Course.order)
    ).all()
    lang = get_language(request)
    cards = []
    for course in courses:
        display_course = localize_course(course, lang)
        accessible_slugs = [
            lesson.slug
            for lesson in display_course.lessons
            if can_access_lesson(user, lesson, display_course)
        ]
        question_count = len(course_questions(course.slug, accessible_slugs, lang))
        if question_count:
            cards.append(
                {
                    "course": display_course,
                    "question_count": question_count,
                    "round_size": min(12, question_count),
                }
            )
    return templates.TemplateResponse(
        request,
        "challenges.html",
        {"request": request, "user": user, "cards": cards},
    )


@router.get("/courses/{course_slug}", response_class=HTMLResponse)
def course_detail(
    course_slug: str,
    request: Request,
    db: Session = Depends(get_db),
    user=Depends(current_user_optional),
):
    if not is_published_course(course_slug):
        return templates.TemplateResponse(
            request, "errors/404.html", {"request": request, "user": user}, status_code=404
        )
    course = db.scalar(select(Course).where(Course.slug == course_slug))
    if course is None:
        return templates.TemplateResponse(
            request, "errors/404.html", {"request": request, "user": user}, status_code=404
        )
    done_ids = completed_lesson_ids(db, user) if user else set()
    done, total, percent = course_progress(db, user, course)
    lang = get_language(request)
    display_course = localize_course(course, lang)
    has_practice = any(
        get_quiz(course.slug, lesson.slug, lang) for lesson in display_course.lessons
    )
    lessons = []
    for lesson in display_course.lessons:
        lessons.append(
            {
                "lesson": lesson,
                "accessible": can_access_lesson(user, lesson, display_course),
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
            "course": display_course,
            "lessons": lessons,
            "done": done,
            "total": total,
            "percent": percent,
            "has_practice": has_practice,
        },
    )


# NOTE: registered before /courses/{course_slug}/{lesson_slug} so "practice"
# is not treated as a lesson slug.
@router.get("/courses/{course_slug}/practice", response_class=HTMLResponse)
def practice(
    course_slug: str,
    request: Request,
    db: Session = Depends(get_db),
    user: User = Depends(require_user),
):
    if not is_published_course(course_slug):
        return templates.TemplateResponse(
            request, "errors/404.html", {"request": request, "user": user}, status_code=404
        )
    course = db.scalar(select(Course).where(Course.slug == course_slug))
    if course is None:
        return templates.TemplateResponse(
            request, "errors/404.html", {"request": request, "user": user}, status_code=404
        )

    lang = get_language(request)
    display_course = localize_course(course, lang)
    accessible_slugs = [
        lesson.slug
        for lesson in display_course.lessons
        if can_access_lesson(user, lesson, display_course)
    ]
    pool = course_questions(course.slug, accessible_slugs, lang)
    random.shuffle(pool)
    questions = pool[:12]

    return templates.TemplateResponse(
        request,
        "practice.html",
        {
            "request": request,
            "user": user,
            "course": display_course,
            "quiz": {"questions": questions, "pass_percent": 0} if questions else None,
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
    if not is_published_course(course_slug):
        return templates.TemplateResponse(
            request, "errors/404.html", {"request": request, "user": user}, status_code=404
        )
    course, lesson = _load_lesson(db, course_slug, lesson_slug)
    if course is None or lesson is None:
        return templates.TemplateResponse(
            request, "errors/404.html", {"request": request, "user": user}, status_code=404
        )

    if not can_access_lesson(user, lesson, course):
        display_course = localize_course(course, get_language(request))
        display_lesson = next(
            (item for item in display_course.lessons if item.slug == lesson.slug),
            lesson,
        )
        return templates.TemplateResponse(
            request,
            "lesson_locked.html",
            {"request": request, "user": user, "course": display_course, "lesson": display_lesson},
            status_code=403,
        )

    idx = lesson_index(lesson, course)
    display_course = localize_course(course, get_language(request))
    lessons = display_course.lessons
    lesson = lessons[idx]
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

    lang = get_language(request)
    quiz = get_quiz(course.slug, lesson.slug, lang)
    activities = get_activities(course.slug, lesson.slug, lang)
    lesson_outline = []
    for position, outline_lesson in enumerate(lessons, start=1):
        lesson_outline.append(
            {
                "lesson": outline_lesson,
                "number": position,
                "current": outline_lesson.id == lesson.id,
                "completed": outline_lesson.id in done_ids,
                "accessible": can_access_lesson(user, outline_lesson, display_course),
            }
        )
    quiz_result = None
    if user and quiz:
        db_lesson = db.get(Lesson, lesson.id)
        quiz_result = get_quiz_result(db, user, db_lesson)

    return templates.TemplateResponse(
        request,
        "lesson.html",
        {
            "request": request,
            "user": user,
            "course": display_course,
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
            "quiz": quiz,
            "activities": activities,
            "lesson_outline": lesson_outline,
            "course_points": done * 100,
            "quiz_passed": bool(quiz_result and quiz_result.passed),
            "quiz_result_url": f"/courses/{course.slug}/{lesson.slug}/quiz/result",
        },
    )


class QuizResultIn(BaseModel):
    score: int


@router.post("/courses/{course_slug}/{lesson_slug}/quiz/result")
def submit_quiz_result(
    course_slug: str,
    lesson_slug: str,
    payload: QuizResultIn,
    request: Request,
    db: Session = Depends(get_db),
    user: User = Depends(require_user),
):
    course, lesson = _load_lesson(db, course_slug, lesson_slug)
    if course is None or lesson is None:
        return JSONResponse({"error": "not found"}, status_code=404)
    if not can_access_lesson(user, lesson, course):
        return JSONResponse({"error": "forbidden"}, status_code=403)

    quiz = get_quiz(course_slug, lesson_slug, get_language(request))
    if quiz is None:
        return JSONResponse({"error": "no quiz"}, status_code=404)

    # The client grades for instant feedback; the server owns the bounds.
    total = len(quiz["questions"])
    score = max(0, min(payload.score, total))
    result = save_quiz_result(db, user, lesson, score, total, quiz["pass_percent"])
    return {"passed": result.passed, "best_score": result.score, "total": result.total}


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
