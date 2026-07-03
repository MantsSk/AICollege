import os
import tempfile

import pytest

# Configure an isolated SQLite database BEFORE importing the app/config.
_DB = os.path.join(tempfile.gettempdir(), "aicollege_pytest.db")
if os.path.exists(_DB):
    os.remove(_DB)
os.environ["DATABASE_URL"] = f"sqlite:///{_DB}"
os.environ["SECRET_KEY"] = "test-secret"
os.environ["DEBUG"] = "true"
os.environ["FREE_DAILY_AI_MESSAGES"] = "2"
os.environ["FREE_LESSONS_PER_COURSE"] = "2"

import app.config as config  # noqa: E402

config.get_settings.cache_clear()
config.settings = config.get_settings()

from app.database import Base, engine  # noqa: E402
import app.models  # noqa: E402,F401
from app.seed import seed  # noqa: E402
from app.main import app as fastapi_app  # noqa: E402


@pytest.fixture(scope="session", autouse=True)
def _setup_db():
    Base.metadata.create_all(engine)
    seed()
    yield


@pytest.fixture
def client():
    from fastapi.testclient import TestClient

    return TestClient(fastapi_app)


@pytest.fixture
def mock_mentor(monkeypatch):
    import app.routers.ai as ai_router

    monkeypatch.setattr(ai_router, "ask_mentor", lambda messages, lang="lt": "Mock reply with `code`.")
