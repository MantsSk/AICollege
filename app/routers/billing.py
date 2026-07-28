import logging

from fastapi import APIRouter, Depends, Header, Request
from fastapi.responses import HTMLResponse, RedirectResponse

from sqlalchemy.orm import Session

from app import billing
from app.config import settings
from app.database import get_db
from app.deps import require_user
from app.models import User

router = APIRouter(prefix="/billing")
logger = logging.getLogger(__name__)


@router.post("/checkout")
def checkout(request: Request, db: Session = Depends(get_db), user: User = Depends(require_user)):
    if not settings.payments_enabled:
        return HTMLResponse("Payments are disabled for testing.", status_code=503)
    if not settings.stripe_secret_key or not settings.stripe_price_id:
        return HTMLResponse(
            "Stripe is not configured. Set STRIPE_SECRET_KEY and STRIPE_PRICE_ID.",
            status_code=503,
        )
    if user.is_subscribed:
        return RedirectResponse("/dashboard", status_code=303)
    url = billing.create_checkout_session(db, user)
    return RedirectResponse(url, status_code=303)


@router.post("/portal")
def portal(request: Request, db: Session = Depends(get_db), user: User = Depends(require_user)):
    if not settings.payments_enabled:
        return HTMLResponse("Payments are disabled for testing.", status_code=503)
    if not settings.stripe_secret_key:
        return HTMLResponse("Stripe is not configured.", status_code=503)
    url = billing.create_billing_portal_session(db, user)
    return RedirectResponse(url, status_code=303)


@router.post("/webhook")
async def webhook(
    request: Request,
    stripe_signature: str = Header(None, alias="Stripe-Signature"),
    db: Session = Depends(get_db),
):
    if not settings.payments_enabled:
        return HTMLResponse("Payments are disabled for testing.", status_code=503)
    payload = await request.body()
    try:
        billing.handle_webhook(db, payload, stripe_signature or "")
    except Exception:  # noqa: BLE001
        # Signature and provider errors may include implementation details.
        logger.exception("Stripe webhook processing failed")
        return HTMLResponse("Invalid webhook.", status_code=400)
    return {"received": True}
