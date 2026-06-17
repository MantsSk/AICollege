"""Password hashing and current-user resolution from the session."""
from __future__ import annotations

from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
    return pwd_context.verify(password, password_hash)


def get_current_user(request, db: Session) -> User | None:
    """Return the logged-in User from the session, or None."""
    user_id = request.session.get("user_id")
    if not user_id:
        return None
    return db.get(User, user_id)
