import secrets
from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.config import settings
from app.database import get_db
from app.deps import current_user_optional
from app.models import User
from app.security import hash_password, verify_password
from app.templating import templates

router = APIRouter()


def _redirect(url: str) -> RedirectResponse:
    return RedirectResponse(url, status_code=303)


@router.get("/register", response_class=HTMLResponse)
def register_form(request: Request, user=Depends(current_user_optional)):
    if user:
        return _redirect("/dashboard")
    return templates.TemplateResponse(
        request, "auth/register.html", {"request": request, "user": None}
    )


@router.post("/register", response_class=HTMLResponse)
def register(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    full_name: str = Form(""),
    db: Session = Depends(get_db),
):
    email = email.strip().lower()
    error = None
    if len(password) < 8:
        error = "Password must be at least 8 characters."
    elif db.scalar(select(User).where(User.email == email)):
        error = "An account with this email already exists."

    if error:
        return templates.TemplateResponse(
            request,
            "auth/register.html",
            {"request": request, "user": None, "error": error, "email": email},
            status_code=400,
        )

    user = User(email=email, password_hash=hash_password(password), full_name=full_name.strip() or None)
    db.add(user)
    db.commit()
    request.session["user_id"] = user.id
    return _redirect("/dashboard")


@router.get("/login", response_class=HTMLResponse)
def login_form(request: Request, user=Depends(current_user_optional)):
    if user:
        return _redirect("/dashboard")
    return templates.TemplateResponse(
        request, "auth/login.html", {"request": request, "user": None}
    )


@router.post("/login", response_class=HTMLResponse)
def login(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    email = email.strip().lower()
    user = db.scalar(select(User).where(User.email == email))
    if user is None or not verify_password(password, user.password_hash):
        return templates.TemplateResponse(
            request,
            "auth/login.html",
            {"request": request, "user": None, "error": "Invalid email or password.", "email": email},
            status_code=400,
        )
    request.session["user_id"] = user.id
    return _redirect("/dashboard")


@router.post("/logout")
@router.get("/logout")
def logout(request: Request):
    request.session.clear()
    return _redirect("/")


# --- Password reset -------------------------------------------------------


@router.get("/forgot-password", response_class=HTMLResponse)
def forgot_form(request: Request, user=Depends(current_user_optional)):
    return templates.TemplateResponse(
        request, "auth/forgot.html", {"request": request, "user": None}
    )


@router.post("/forgot-password", response_class=HTMLResponse)
def forgot(request: Request, email: str = Form(...), db: Session = Depends(get_db)):
    email = email.strip().lower()
    user = db.scalar(select(User).where(User.email == email))
    reset_link = None
    if user:
        token = secrets.token_urlsafe(32)
        user.reset_token = token
        user.reset_token_expires = datetime.now(timezone.utc) + timedelta(hours=1)
        db.commit()
        reset_link = f"{settings.base_url}/reset-password?token={token}"
        # MVP: no email service yet — surface the link in debug so it's usable.
    return templates.TemplateResponse(
        request,
        "auth/forgot.html",
        {
            "request": request,
            "user": None,
            "sent": True,
            "reset_link": reset_link if settings.debug else None,
        },
    )


@router.get("/reset-password", response_class=HTMLResponse)
def reset_form(request: Request, token: str = "", db: Session = Depends(get_db)):
    user = _user_for_token(db, token)
    return templates.TemplateResponse(
        request,
        "auth/reset.html",
        {"request": request, "user": None, "token": token, "valid": user is not None},
    )


@router.post("/reset-password", response_class=HTMLResponse)
def reset(
    request: Request,
    token: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    user = _user_for_token(db, token)
    if user is None:
        return templates.TemplateResponse(
            request,
            "auth/reset.html",
            {"request": request, "user": None, "token": token, "valid": False},
            status_code=400,
        )
    if len(password) < 8:
        return templates.TemplateResponse(
            request,
            "auth/reset.html",
            {
                "request": request,
                "user": None,
                "token": token,
                "valid": True,
                "error": "Password must be at least 8 characters.",
            },
            status_code=400,
        )
    user.password_hash = hash_password(password)
    user.reset_token = None
    user.reset_token_expires = None
    db.commit()
    request.session["user_id"] = user.id
    return _redirect("/dashboard")


def _user_for_token(db: Session, token: str) -> User | None:
    if not token:
        return None
    user = db.scalar(select(User).where(User.reset_token == token))
    if user is None or user.reset_token_expires is None:
        return None
    expires = user.reset_token_expires
    # Some DB backends (e.g. SQLite) return naive datetimes; normalize to UTC-aware.
    if expires.tzinfo is None:
        expires = expires.replace(tzinfo=timezone.utc)
    if expires < datetime.now(timezone.utc):
        return None
    return user
