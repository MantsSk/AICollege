import re
import uuid


def _register(client, email=None, password="password123"):
    email = email or f"{uuid.uuid4().hex[:8]}@test.com"
    client.post("/register", data={"email": email, "password": password})
    return email


def test_public_pages(client):
    for path in ("/", "/pricing", "/courses", "/courses/python-basics", "/healthz"):
        assert client.get(path).status_code == 200


def test_anonymous_lesson_gating(client):
    # First lesson is public, second is locked for anonymous visitors.
    assert client.get("/courses/python-basics/lesson-01").status_code == 200
    assert client.get("/courses/python-basics/lesson-02").status_code == 403


def test_dashboard_requires_login(client):
    r = client.get("/dashboard", follow_redirects=False)
    assert r.status_code == 303
    assert r.headers["location"] == "/login"


def test_register_and_free_tier(client):
    _register(client)
    # Nemokamas vartotojas gauna pirmas 2 pamokas, trečia užrakinta.
    assert client.get("/courses/python-basics/lesson-02").status_code == 200
    assert client.get("/courses/python-basics/lesson-03").status_code == 403


def test_login_flow(client):
    email = _register(client)
    client.get("/logout")
    assert client.post(
        "/login", data={"email": email, "password": "password123"}, follow_redirects=False
    ).status_code == 303
    assert client.post(
        "/login", data={"email": email, "password": "nope"}
    ).status_code == 400


def test_password_reset(client):
    email = _register(client)
    client.get("/logout")
    r = client.post("/forgot-password", data={"email": email})
    token = re.search(r"token=([A-Za-z0-9_\-]+)", r.text).group(1)
    assert client.post(
        "/reset-password",
        data={"token": token, "password": "newpassword123"},
        follow_redirects=False,
    ).status_code == 303


def test_mark_complete(client):
    _register(client)
    r = client.post("/courses/python-basics/lesson-01/complete")
    assert r.status_code == 200
    assert "baigta" in r.text.lower()


def test_billing_unconfigured(client):
    _register(client)
    assert client.post("/billing/checkout", follow_redirects=False).status_code == 503


def test_ai_mentor_and_limit(client, mock_mentor):
    _register(client)
    r = client.post("/mentor/python-basics/lesson-01", data={"message": "hello"})
    assert "Mock reply" in r.text
    client.post("/mentor/python-basics/lesson-01", data={"message": "again"})
    r3 = client.post("/mentor/python-basics/lesson-01", data={"message": "third"})
    assert "dienos DI mentoriaus limitą" in r3.text


def test_markdown_rendering(client):
    r = client.get("/courses/python-basics/lesson-01")
    assert "codehilite" in r.text  # syntax-highlighted code block
    assert "DI mentorius" in r.text
