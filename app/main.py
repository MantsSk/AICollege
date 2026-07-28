import hmac
import secrets
from urllib.parse import urlparse

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
from starlette.middleware.sessions import SessionMiddleware

from app.config import settings
from app.routers import ai, auth, billing, courses, pages
from app.templating import templates, TEMPLATES_DIR  # noqa: F401

settings.validate_for_runtime()

app = FastAPI(title=settings.app_name, debug=settings.debug)


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response.headers.setdefault("X-Content-Type-Options", "nosniff")
        response.headers.setdefault("X-Frame-Options", "DENY")
        response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
        response.headers.setdefault(
            "Permissions-Policy",
            "camera=(), microphone=(), geolocation=(), payment=()",
        )
        if request.url.scheme == "https":
            response.headers.setdefault(
                "Strict-Transport-Security",
                "max-age=31536000; includeSubDomains",
            )
        return response


class SameOriginPostMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.method in {"POST", "PUT", "PATCH", "DELETE"}:
            origin = request.headers.get("origin")
            if origin:
                origin_host = urlparse(origin).netloc
                allowed_hosts = {urlparse(settings.base_url).netloc, request.url.netloc}
                if origin_host not in allowed_hosts:
                    return HTMLResponse("Forbidden", status_code=403)
        return await call_next(request)


class CsrfMiddleware(BaseHTTPMiddleware):
    """Require a session-bound token for browser state-changing requests."""

    _SAFE_METHODS = {"GET", "HEAD", "OPTIONS"}
    _EXEMPT_PATHS = {"/billing/webhook"}  # Stripe uses its own signed payload.

    async def dispatch(self, request: Request, call_next):
        token = request.session.setdefault("csrf_token", secrets.token_urlsafe(32))
        if request.method not in self._SAFE_METHODS and request.url.path not in self._EXEMPT_PATHS:
            supplied = request.headers.get("X-CSRF-Token")
            if not supplied:
                # Cache the body before form-parsing so the downstream
                # endpoint can still read it (parsing alone consumes the stream).
                await request.body()
                form = await request.form()
                supplied = form.get("csrf_token")
            if not supplied or not hmac.compare_digest(token, supplied):
                return HTMLResponse("Forbidden", status_code=403)
        return await call_next(request)


app.add_middleware(SecurityHeadersMiddleware)
app.add_middleware(SameOriginPostMiddleware)
app.add_middleware(TrustedHostMiddleware, allowed_hosts=settings.allowed_host_list)
app.add_middleware(CsrfMiddleware)

if settings.secure_ssl_redirect:
    app.add_middleware(HTTPSRedirectMiddleware)

app.add_middleware(
    SessionMiddleware,
    secret_key=settings.secret_key,
    https_only=not settings.debug,
    same_site="lax",
    max_age=60 * 60 * 24 * 14,  # 14 days
)

app.mount(
    "/static",
    StaticFiles(directory=str(TEMPLATES_DIR.parent / "static")),
    name="static",
)

app.include_router(pages.router)
app.include_router(auth.router)
app.include_router(courses.router)
app.include_router(ai.router)
app.include_router(billing.router)


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.exception_handler(404)
async def not_found(request: Request, exc):
    return templates.TemplateResponse(
        request, "errors/404.html", {"request": request, "user": None}, status_code=404
    )
