"""Stripe subscription integration: checkout, billing portal, webhook sync."""
from __future__ import annotations

from datetime import datetime, timezone

import stripe
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.config import settings
from app.models import Subscription, User

stripe.api_key = settings.stripe_secret_key


def _get_or_create_subscription(db: Session, user: User) -> Subscription:
    sub = user.subscription
    if sub is None:
        sub = Subscription(user_id=user.id, status="none")
        db.add(sub)
        db.commit()
        db.refresh(sub)
    return sub


def _ensure_customer(db: Session, user: User) -> str:
    sub = _get_or_create_subscription(db, user)
    if sub.stripe_customer_id:
        return sub.stripe_customer_id
    customer = stripe.Customer.create(email=user.email, metadata={"user_id": str(user.id)})
    sub.stripe_customer_id = customer.id
    db.commit()
    return customer.id


def create_checkout_session(db: Session, user: User) -> str:
    """Create a Stripe Checkout session and return its URL."""
    customer_id = _ensure_customer(db, user)
    session = stripe.checkout.Session.create(
        mode="subscription",
        customer=customer_id,
        line_items=[{"price": settings.stripe_price_id, "quantity": 1}],
        success_url=f"{settings.base_url}/dashboard?upgraded=1",
        cancel_url=f"{settings.base_url}/pricing",
        allow_promotion_codes=True,
        metadata={"user_id": str(user.id)},
    )
    return session.url


def create_billing_portal_session(db: Session, user: User) -> str:
    customer_id = _ensure_customer(db, user)
    session = stripe.billing_portal.Session.create(
        customer=customer_id,
        return_url=f"{settings.base_url}/dashboard",
    )
    return session.url


def _apply_subscription(db: Session, sub_obj: dict) -> None:
    """Update our Subscription row from a Stripe subscription object/dict."""
    customer_id = sub_obj.get("customer")
    sub = db.scalar(
        select(Subscription).where(Subscription.stripe_customer_id == customer_id)
    )
    if sub is None:
        # Fall back to metadata.user_id if present.
        user_id = (sub_obj.get("metadata") or {}).get("user_id")
        if user_id:
            user = db.get(User, int(user_id))
            if user:
                sub = _get_or_create_subscription(db, user)
                sub.stripe_customer_id = customer_id
    if sub is None:
        return

    sub.stripe_subscription_id = sub_obj.get("id")
    sub.status = sub_obj.get("status", "none")
    sub.cancel_at_period_end = bool(sub_obj.get("cancel_at_period_end"))
    period_end = sub_obj.get("current_period_end")
    if period_end:
        sub.current_period_end = datetime.fromtimestamp(period_end, tz=timezone.utc)
    db.commit()


def handle_webhook(db: Session, payload: bytes, sig_header: str) -> None:
    """Verify and process a Stripe webhook event."""
    event = stripe.Webhook.construct_event(
        payload, sig_header, settings.stripe_webhook_secret
    )
    etype = event["type"]
    obj = event["data"]["object"]

    if etype == "checkout.session.completed":
        sub_id = obj.get("subscription")
        customer_id = obj.get("customer")
        if sub_id:
            stripe_sub = stripe.Subscription.retrieve(sub_id)
            data = dict(stripe_sub)
            data.setdefault("customer", customer_id)
            data.setdefault("metadata", obj.get("metadata") or {})
            _apply_subscription(db, data)
    elif etype in (
        "customer.subscription.created",
        "customer.subscription.updated",
        "customer.subscription.deleted",
    ):
        _apply_subscription(db, dict(obj))
