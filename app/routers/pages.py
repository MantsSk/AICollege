from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.course_paths import PUBLISHED_COURSE_SLUGS, group_by_path
from app.database import get_db
from app.deps import current_user_optional, require_user
from app.course_i18n import localize_course, localize_courses
from app.i18n import SUPPORTED_LANGUAGES, get_language
from app.models import Course, QuizResult, User
from app.services import completed_lesson_ids, course_progress
from app.templating import templates

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def landing(request: Request, db: Session = Depends(get_db), user=Depends(current_user_optional)):
    courses = db.scalars(
        select(Course)
        .where(Course.slug.in_(PUBLISHED_COURSE_SLUGS))
        .order_by(Course.order)
    ).all()
    courses = localize_courses(courses, get_language(request))
    path_sections = group_by_path([{"course": course} for course in courses])
    return templates.TemplateResponse(
        request,
        "landing.html",
        {
            "request": request,
            "user": user,
            "courses": courses,
            "path_sections": path_sections,
        },
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
    courses = db.scalars(
        select(Course)
        .where(Course.slug.in_(PUBLISHED_COURSE_SLUGS))
        .order_by(Course.order)
    ).all()
    lang = get_language(request)
    done_ids = completed_lesson_ids(db, user)

    course_cards = []
    continue_target = None
    for course in courses:
        done, total, percent = course_progress(db, user, course)
        display_course = localize_course(course, lang)
        # find first not-completed lesson to "continue"
        next_lesson = None
        for lesson in display_course.lessons:
            if lesson.id not in done_ids:
                next_lesson = lesson
                break
        card = {
            "course": display_course,
            "done": done,
            "total": total,
            "percent": percent,
            "next_lesson": next_lesson or (display_course.lessons[-1] if display_course.lessons else None),
        }
        course_cards.append(card)
        if continue_target is None and percent > 0 and percent < 100 and next_lesson:
            continue_target = card
    path_sections = group_by_path(course_cards)
    passed_checks = db.scalar(
        select(func.count()).select_from(QuizResult).where(
            QuizResult.user_id == user.id, QuizResult.passed.is_(True)
        )
    ) or 0
    learner_stats = {
        "lessons": len(done_ids),
        "checks": passed_checks,
        # Keep the score legible: every completed lesson is worth 100 points.
        "points": len(done_ids) * 100,
    }

    return templates.TemplateResponse(
        request,
        "dashboard.html",
        {
            "request": request,
            "user": user,
            "course_cards": course_cards,
            "path_sections": path_sections,
            "continue_target": continue_target,
            "upgraded": bool(upgraded),
            "learner_stats": learner_stats,
        },
    )


@router.get("/language/{lang}")
def set_language(lang: str, request: Request, next: str = "/"):
    if lang not in SUPPORTED_LANGUAGES:
        lang = "lt"
    if not next.startswith("/"):
        next = "/"
    response = RedirectResponse(next, status_code=303)
    response.set_cookie(
        "language",
        lang,
        max_age=60 * 60 * 24 * 365,
        httponly=False,
        samesite="lax",
    )
    return response
