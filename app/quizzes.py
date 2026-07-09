"""Load per-lesson quizzes from JSON files on disk.

Quizzes live next to the lesson markdown they belong to:

    courses/<course-slug>/lesson-01.quiz.json           # canonical (LT)
    courses_i18n/<lang>/<course-slug>/lesson-01.quiz.json  # display overlay

Like lesson content, the canonical files are the source of truth and the
overlay directory only replaces what it provides — a missing overlay falls
back to the canonical quiz.

Question types (SoloLearn-style):

    single     one correct option            options + answer (index)
    multi      several correct options       options + answers (indexes)
    truefalse  true/false statement          answer (bool)
    fill       type the missing word         code with __ + accept (list of strings)
    gap        tap words into code blanks    code with __ + bank + gaps (correct words, in order)
    order      arrange lines in order        items (given in correct order)

Every question has "prompt", optionally "code" and "explain".
"""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

from app.content import COURSES_DIR
from app.course_i18n import COURSE_I18N_DIR

QUESTION_TYPES = {"single", "multi", "truefalse", "fill", "gap", "order"}
DEFAULT_PASS_PERCENT = 70


class QuizError(ValueError):
    """Raised for malformed quiz files so bad content fails loudly in dev."""


def _validate(quiz: dict, source: Path) -> dict:
    questions = quiz.get("questions")
    if not isinstance(questions, list) or not questions:
        raise QuizError(f"{source}: 'questions' must be a non-empty list")
    for i, q in enumerate(questions):
        where = f"{source}: question {i + 1}"
        qtype = q.get("type")
        if qtype not in QUESTION_TYPES:
            raise QuizError(f"{where}: unknown type {qtype!r}")
        if not q.get("prompt"):
            raise QuizError(f"{where}: missing prompt")
        if qtype in ("single", "multi"):
            options = q.get("options")
            if not isinstance(options, list) or len(options) < 2:
                raise QuizError(f"{where}: needs at least 2 options")
            if qtype == "single":
                if not isinstance(q.get("answer"), int) or not 0 <= q["answer"] < len(options):
                    raise QuizError(f"{where}: 'answer' must index into options")
            else:
                answers = q.get("answers")
                if (
                    not isinstance(answers, list)
                    or not answers
                    or not all(isinstance(a, int) and 0 <= a < len(options) for a in answers)
                ):
                    raise QuizError(f"{where}: 'answers' must be a list of option indexes")
        elif qtype == "truefalse":
            if not isinstance(q.get("answer"), bool):
                raise QuizError(f"{where}: 'answer' must be true or false")
        elif qtype == "fill":
            accept = q.get("accept")
            if not isinstance(accept, list) or not all(isinstance(a, str) and a for a in accept):
                raise QuizError(f"{where}: 'accept' must be a list of strings")
            if (q.get("code") or "").count("__") != 1:
                raise QuizError(f"{where}: 'code' must contain exactly one __ blank")
        elif qtype == "gap":
            gaps = q.get("gaps")
            bank = q.get("bank")
            if not isinstance(gaps, list) or not gaps:
                raise QuizError(f"{where}: 'gaps' must be a non-empty list")
            if not isinstance(bank, list) or len(bank) < len(gaps):
                raise QuizError(f"{where}: 'bank' must contain at least the gap words")
            if (q.get("code") or "").count("__") != len(gaps):
                raise QuizError(f"{where}: 'code' must have one __ per gap")
            missing = [w for w in gaps if w not in bank]
            if missing:
                raise QuizError(f"{where}: gap words {missing} missing from bank")
        elif qtype == "order":
            items = q.get("items")
            if not isinstance(items, list) or len(items) < 2:
                raise QuizError(f"{where}: 'items' needs at least 2 entries")
    quiz.setdefault("pass_percent", DEFAULT_PASS_PERCENT)
    return quiz


@lru_cache(maxsize=None)
def _load_quiz_file(path: Path) -> dict | None:
    if not path.exists():
        return None
    quiz = json.loads(path.read_text(encoding="utf-8"))
    return _validate(quiz, path)


def get_quiz(course_slug: str, lesson_slug: str, lang: str) -> dict | None:
    """Return the quiz for a lesson in the requested language, or None."""
    name = f"{lesson_slug}.quiz.json"
    if lang != "lt":
        overlay = _load_quiz_file(COURSE_I18N_DIR / lang / course_slug / name)
        if overlay is not None:
            return overlay
    return _load_quiz_file(COURSES_DIR / course_slug / name)


def course_questions(course_slug: str, lesson_slugs: list[str], lang: str) -> list[dict]:
    """Pool every quiz question of the given lessons (for practice mode)."""
    pool: list[dict] = []
    for slug in lesson_slugs:
        quiz = get_quiz(course_slug, slug, lang)
        if quiz:
            pool.extend(quiz["questions"])
    return pool
