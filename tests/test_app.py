import re
import uuid


def _register(client, email=None, password="password123"):
    email = email or f"{uuid.uuid4().hex[:8]}@test.com"
    _post(client, "/register", data={"email": email, "password": password})
    return email


def _post(client, url, *, data=None, **kwargs):
    page = client.get("/")
    token = re.search(r'<meta name="csrf-token" content="([^"]+)"', page.text).group(1)
    headers = kwargs.pop("headers", {})
    return client.post(url, data=data, headers={**headers, "X-CSRF-Token": token}, **kwargs)


def test_public_pages(client):
    for path in (
        "/",
        "/pricing",
        "/courses",
        "/challenges",
        "/courses/practical-ai",
        "/courses/practical-ai/lesson-00",
        "/courses/python-basics",
        "/healthz",
    ):
        assert client.get(path).status_code == 200


def test_mission_course_exposes_workbench_and_profile(client):
    course = client.get("/courses/practical-ai")
    assert "Misijų laboratorija" in course.text
    assert "Patikrinto DI asistento specifikacija" in course.text

    mission = client.get("/courses/practical-ai/lesson-00")
    assert 'data-lesson-activities' in mission.text
    assert '"artifact_builder"' in mission.text
    assert "Patikimumo misija" in mission.text
    assert 'class="course-outline"' in mission.text
    assert 'class="lesson-workspace-tabs"' in mission.text


def test_challenges_catalog_uses_course_question_banks(client):
    page = client.get("/challenges")
    assert page.status_code == 200
    assert "Iššūkiai" in page.text
    assert "Python programavimo mokymai" in page.text


def test_mission_activity_files_validate():
    from app.activities import get_activities

    expected = {
        "lesson-00": {"decision", "diagnose", "artifact_builder"},
        "lesson-01": {"decision", "artifact_builder"},
        "lesson-02": {"decision", "artifact_builder"},
    }
    for lesson_slug, activity_types in expected.items():
        payload = get_activities("practical-ai", lesson_slug, "lt")
        assert payload is not None
        assert {item["type"] for item in payload["activities"]} == activity_types


def test_state_changing_requests_require_csrf_token(client):
    r = client.post("/register", data={"email": "csrf@test.com", "password": "password123"})
    assert r.status_code == 403


def test_form_field_csrf_token_preserves_body(client):
    # Browser forms send the token as a form field (added by app.js), which the
    # middleware parses; the endpoint must still see the rest of the body.
    page = client.get("/login")
    token = re.search(r'<meta name="csrf-token" content="([^"]+)"', page.text).group(1)
    r = client.post(
        "/login",
        data={"email": "nobody@test.com", "password": "wrongpass", "csrf_token": token},
    )
    # 400 invalid-credentials proves the email/password fields reached the endpoint.
    assert r.status_code == 400


def test_anonymous_lesson_gating(client):
    # First lesson is public, second is locked for anonymous visitors.
    assert client.get("/courses/python-basics/lesson-00").status_code == 200
    assert client.get("/courses/python-basics/lesson-01").status_code == 403


def test_dashboard_requires_login(client):
    r = client.get("/dashboard", follow_redirects=False)
    assert r.status_code == 303
    assert r.headers["location"] == "/login"


def test_registered_account_unlocks_courses(client):
    _register(client)
    # Payments are disabled for testing, so an account unlocks full courses.
    assert client.get("/courses/python-basics/lesson-02").status_code == 200
    assert client.get("/courses/python-basics/lesson-03").status_code == 200


def test_login_flow(client):
    email = _register(client)
    _post(client, "/logout")
    assert _post(
        client, "/login", data={"email": email, "password": "password123"}, follow_redirects=False
    ).status_code == 303
    assert _post(
        client, "/login", data={"email": email, "password": "nope"}
    ).status_code == 400


def test_password_reset(client):
    email = _register(client)
    _post(client, "/logout")
    r = _post(client, "/forgot-password", data={"email": email})
    token = re.search(r"token=([A-Za-z0-9_\-]+)", r.text).group(1)
    assert _post(
        client, "/reset-password",
        data={"token": token, "password": "newpassword123"},
        follow_redirects=False,
    ).status_code == 303


def test_mark_complete(client):
    _register(client)
    r = _post(client, "/courses/python-basics/lesson-01/complete")
    assert r.status_code == 200
    assert "baigta" in r.text.lower()


def test_billing_disabled(client):
    _register(client)
    r = _post(client, "/billing/checkout", follow_redirects=False)
    assert r.status_code == 503
    assert "Payments are disabled" in r.text


def test_ai_mentor_and_limit(client, mock_mentor):
    _register(client)
    r = _post(client, "/mentor/python-basics/lesson-01", data={"message": "hello"})
    assert "Mock reply" in r.text
    _post(client, "/mentor/python-basics/lesson-01", data={"message": "again"})
    r3 = _post(client, "/mentor/python-basics/lesson-01", data={"message": "third"})
    assert "dienos DI mentoriaus limitą" in r3.text


def test_markdown_rendering(client):
    _register(client)
    r = client.get("/courses/python-basics/lesson-01")
    assert "codehilite" in r.text  # syntax-highlighted code block
    assert "DI mentorius" in r.text
