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
        "/courses/python-basics",
        "/courses/python-basics/lesson-00",
        "/courses/practical-ai",
        "/courses/practical-ai/lesson-00",
        "/healthz",
    ):
        assert client.get(path).status_code == 200


def test_landing_copy_is_concise(client):
    page = client.get("/").text
    assert "Išmok Python nuo nulio" in page
    assert "po vieną žingsnį" in page
    assert "Paversk chaosą darbo procesu" not in page
    assert "Kursų katalogas" not in page
    assert "Kaip mokysiesi" not in page
    assert "Pradėk mokytis DI šiandien" not in page
    assert 'href="/courses/python-basics"' in page
    assert 'href="/courses/python-basics/lesson-00"' in page
    assert "DI darbe: patikimas asistentas" in page


def test_python_course_starts_with_two_progressive_lessons(client):
    course = client.get("/courses/python-basics")
    assert course.status_code == 200
    assert "Python nuo nulio" in course.text
    assert course.text.count('href="/courses/python-basics/lesson-00"') == 1
    assert "Kintamieji: duomenims suteik vardus" in course.text

    lesson = client.get("/courses/python-basics/lesson-00")
    assert "Pirmoji Python programa" in lesson.text
    assert "Klaida nėra nesėkmė" in lesson.text
    assert 'class="course-outline"' in lesson.text
    assert 'class="lesson-workspace-tabs"' in lesson.text
    assert 'data-lesson-activities' in lesson.text
    assert '"code_exercise"' in lesson.text

    assert client.get("/courses/python-basics/lesson-01").status_code == 403


def test_second_python_lesson_has_variables_lab(client):
    _register(client)
    lesson = client.get("/courses/python-basics/lesson-01")
    assert lesson.status_code == 200
    assert "Kintamieji: duomenims suteik vardus" in lesson.text
    assert "Kintamojo reikšmę galima pakeisti" in lesson.text
    assert 'data-lesson-activities' in lesson.text
    assert '"code_exercise"' in lesson.text
    assert 'vizitine.py' in lesson.text


def test_ai_course_starts_with_one_practical_lesson(client):
    course = client.get("/courses/practical-ai")
    assert course.status_code == 200
    assert "DI darbe: patikimas asistentas" in course.text
    assert "Patikrintas DI asistentas" in course.text
    assert course.text.count('href="/courses/practical-ai/lesson-00"') == 1

    lesson = client.get("/courses/practical-ai/lesson-00")
    assert lesson.status_code == 200
    assert "Pirmasis geras promptas" in lesson.text
    assert "Keturi gero prompto elementai" in lesson.text
    assert 'data-lesson-activities' in lesson.text
    assert '"prompt_builder"' in lesson.text
    assert client.get("/courses/practical-ai/lesson-01").status_code == 404


def test_challenges_catalog_uses_course_question_banks(client):
    page = client.get("/challenges")
    assert page.status_code == 200
    assert "Iššūkiai" in page.text
    assert "Python nuo nulio" in page.text


def test_lesson_laboratories_are_available():
    from app.activities import get_activities

    ai_payload = get_activities("practical-ai", "lesson-00", "lt")
    assert ai_payload is not None
    assert [activity["type"] for activity in ai_payload["activities"]] == [
        "decision",
        "prompt_builder",
    ]
    payload = get_activities("python-basics", "lesson-00", "lt")
    assert payload is not None
    assert payload["activities"][0]["type"] == "code_exercise"
    assert payload["activities"][0]["file_name"] == "main.py"
    second_payload = get_activities("python-basics", "lesson-01", "lt")
    assert second_payload is not None
    assert second_payload["activities"][0]["type"] == "code_exercise"
    assert second_payload["activities"][0]["file_name"] == "vizitine.py"


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
    # The first and currently only lesson is public.
    assert client.get("/courses/python-basics/lesson-00").status_code == 200
    assert client.get("/courses/python-basics/lesson-01").status_code == 403


def test_dashboard_requires_login(client):
    r = client.get("/dashboard", follow_redirects=False)
    assert r.status_code == 303
    assert r.headers["location"] == "/login"


def test_registered_account_unlocks_courses(client):
    _register(client)
    assert client.get("/courses/python-basics").status_code == 200
    assert client.get("/courses/python-basics/lesson-00").status_code == 200
    assert client.get("/courses/python-basics/lesson-01").status_code == 200


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
    r = _post(client, "/courses/python-basics/lesson-00/complete")
    assert r.status_code == 200
    assert "baigta" in r.text.lower()


def test_billing_disabled(client):
    _register(client)
    r = _post(client, "/billing/checkout", follow_redirects=False)
    assert r.status_code == 503
    assert "Payments are disabled" in r.text


def test_ai_mentor_and_limit(client, mock_mentor):
    _register(client)
    r = _post(client, "/mentor/python-basics/lesson-00", data={"message": "hello"})
    assert "Mock reply" in r.text
    _post(client, "/mentor/python-basics/lesson-00", data={"message": "again"})
    r3 = _post(client, "/mentor/python-basics/lesson-00", data={"message": "third"})
    assert "dienos DI mentoriaus limitą" in r3.text


def test_markdown_rendering(client):
    _register(client)
    r = client.get("/courses/python-basics/lesson-00")
    assert "codehilite" in r.text  # syntax-highlighted code block
    assert "DI mentorius" in r.text
