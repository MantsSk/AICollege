"""Small in-memory rate limiter for public write endpoints."""
from __future__ import annotations

from collections import defaultdict, deque
from time import monotonic

from fastapi import HTTPException, Request, status

_BUCKETS: dict[str, deque[float]] = defaultdict(deque)


def client_ip(request: Request) -> str:
    # Do not trust X-Forwarded-For here. It is client-controlled unless a
    # trusted reverse proxy has explicitly stripped and rewritten it.
    return request.client.host if request.client else "unknown"


def rate_limit(request: Request, *, key: str, limit: int, window_seconds: int) -> None:
    now = monotonic()
    bucket_key = f"{key}:{client_ip(request)}"
    bucket = _BUCKETS[bucket_key]
    while bucket and now - bucket[0] > window_seconds:
        bucket.popleft()
    if len(bucket) >= limit:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too many requests. Please try again soon.",
        )
    bucket.append(now)
