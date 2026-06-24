from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.ai import ask_mentor, build_messages
from app.course_i18n import localize_course
from app.database import get_db
from app.deps import require_user
from app.i18n import get_language
from app.models import ChatConversation, ChatMessage, Course, Lesson, User
from app.services import ai_messages_remaining, can_access_lesson, increment_ai_usage
from app.templating import templates

router = APIRouter(prefix="/mentor")


def _get_conversation(db: Session, user: User, lesson: Lesson) -> ChatConversation:
    convo = db.scalar(
        select(ChatConversation).where(
            ChatConversation.user_id == user.id, ChatConversation.lesson_id == lesson.id
        )
    )
    if convo is None:
        convo = ChatConversation(user_id=user.id, lesson_id=lesson.id)
        db.add(convo)
        db.commit()
        db.refresh(convo)
    return convo


@router.post("/{course_slug}/{lesson_slug}", response_class=HTMLResponse)
def chat(
    course_slug: str,
    lesson_slug: str,
    request: Request,
    message: str = Form(...),
    db: Session = Depends(get_db),
    user: User = Depends(require_user),
):
    course = db.scalar(select(Course).where(Course.slug == course_slug))
    lesson = (
        db.scalar(select(Lesson).where(Lesson.course_id == course.id, Lesson.slug == lesson_slug))
        if course
        else None
    )
    if course is None or lesson is None:
        return HTMLResponse("Not found", status_code=404)

    if not can_access_lesson(user, lesson, course):
        return HTMLResponse("Forbidden", status_code=403)

    message = message.strip()
    if not message:
        return HTMLResponse("", status_code=204)

    remaining = ai_messages_remaining(db, user)
    if remaining <= 0:
        return templates.TemplateResponse(
            request,
            "partials/ai_limit.html",
            {"request": request, "user": user},
        )

    convo = _get_conversation(db, user, lesson)
    history = [{"role": m.role, "content": m.content} for m in convo.messages]
    lang = get_language(request)
    display_course = localize_course(course, lang)
    display_lesson = next(
        (item for item in display_course.lessons if item.slug == lesson.slug),
        lesson,
    )

    messages = build_messages(
        course_title=display_course.title,
        module_title=display_lesson.module,
        lesson_title=display_lesson.title,
        lesson_content=display_lesson.content_md,
        history=history,
        user_message=message,
        lang=lang,
    )
    reply = ask_mentor(messages, lang=lang)

    db.add(ChatMessage(conversation_id=convo.id, role="user", content=message))
    db.add(ChatMessage(conversation_id=convo.id, role="assistant", content=reply))
    db.commit()
    increment_ai_usage(db, user)

    return templates.TemplateResponse(
        request,
        "partials/ai_messages.html",
        {
            "request": request,
            "user": user,
            "user_message": message,
            "assistant_message": reply,
            "remaining": ai_messages_remaining(db, user),
        },
    )
