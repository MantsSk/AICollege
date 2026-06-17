from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from app.config import settings
from app.routers import ai, auth, billing, courses, pages
from app.templating import templates, TEMPLATES_DIR  # noqa: F401

app = FastAPI(title=settings.app_name, debug=settings.debug)

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
