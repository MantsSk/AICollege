from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.deps import current_user_optional, require_user
from app.models import Course, User
from app.services import completed_lesson_ids, course_progress
from app.templating import templates

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def landing(request: Request, db: Session = Depends(get_db), user=Depends(current_user_optional)):
    courses = db.scalars(select(Course).order_by(Course.order)).all()
    return templates.TemplateResponse(
        request,
        "landing.html",
        {"request": request, "user": user, "courses": courses},
    )


@router.get("/pricing", response_class=HTMLResponse)
def pricing(request: Request, user=Depends(current_user_optional)):
    return templates.TemplateResponse(
        request, "pricing.html", {"request": request, "user": user}
    )


@router.get("/dashboard", response_class=HTMLResponse)
def dashboard(
    request: Request,
    db: Session = Depends(get_db),
    user: User = Depends(require_user),
    upgraded: int = 0,
):
    courses = db.scalars(select(Course).order_by(Course.order)).all()
    done_ids = completed_lesson_ids(db, user)

    course_cards = []
    continue_target = None
    for course in courses:
        done, total, percent = course_progress(db, user, course)
        # find first not-completed lesson to "continue"
        next_lesson = None
        for lesson in course.lessons:
            if lesson.id not in done_ids:
                next_lesson = lesson
                break
        card = {
            "course": course,
            "done": done,
            "total": total,
            "percent": percent,
            "next_lesson": next_lesson or (course.lessons[-1] if course.lessons else None),
        }
        course_cards.append(card)
        if continue_target is None and percent > 0 and percent < 100 and next_lesson:
            continue_target = card

    return templates.TemplateResponse(
        request,
        "dashboard.html",
        {
            "request": request,
            "user": user,
            "course_cards": course_cards,
            "continue_target": continue_target,
            "upgraded": bool(upgraded),
        },
    )
