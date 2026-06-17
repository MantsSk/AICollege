"""Load course content from markdown files on disk.

Layout:

    courses/
      <course-slug>/
        course.yml            # optional: title, description, order
        lesson-01.md          # frontmatter: title, module, order
        lesson-02.md
        ...

Lesson markdown frontmatter (simple key: value, between --- fences):

    ---
    title: Variables and Types
    module: Variables
    order: 1
    ---
    # markdown body...
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

COURSES_DIR = Path(__file__).resolve().parent.parent / "courses"

_FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", re.DOTALL)


@dataclass
class LessonFile:
    slug: str
    title: str
    module: str
    order: int
    content_md: str


@dataclass
class CourseDir:
    slug: str
    title: str
    description: str
    order: int
    lessons: list[LessonFile] = field(default_factory=list)


def _parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    match = _FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    raw, body = match.group(1), match.group(2)
    meta: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            meta[key.strip().lower()] = value.strip().strip("'\"")
    return meta, body


def _parse_course_meta(course_path: Path) -> dict[str, str]:
    meta_file = course_path / "course.yml"
    meta: dict[str, str] = {}
    if meta_file.exists():
        for line in meta_file.read_text(encoding="utf-8").splitlines():
            if ":" in line and not line.strip().startswith("#"):
                key, _, value = line.partition(":")
                meta[key.strip().lower()] = value.strip().strip("'\"")
    return meta


def _humanize(slug: str) -> str:
    return slug.replace("-", " ").replace("_", " ").title()


def load_courses() -> list[CourseDir]:
    """Read every course directory and return structured content."""
    courses: list[CourseDir] = []
    if not COURSES_DIR.exists():
        return courses

    for course_path in sorted(p for p in COURSES_DIR.iterdir() if p.is_dir()):
        meta = _parse_course_meta(course_path)
        course = CourseDir(
            slug=course_path.name,
            title=meta.get("title", _humanize(course_path.name)),
            description=meta.get("description", ""),
            order=int(meta.get("order", 0) or 0),
        )

        lesson_files = sorted(course_path.glob("lesson-*.md"))
        for idx, lf in enumerate(lesson_files, start=1):
            text = lf.read_text(encoding="utf-8")
            fm, body = _parse_frontmatter(text)
            course.lessons.append(
                LessonFile(
                    slug=lf.stem,  # e.g. "lesson-01"
                    title=fm.get("title", _humanize(lf.stem)),
                    module=fm.get("module", ""),
                    order=int(fm.get("order", idx) or idx),
                    content_md=body.strip(),
                )
            )
        course.lessons.sort(key=lambda x: x.order)
        courses.append(course)

    courses.sort(key=lambda c: (c.order, c.title))
    return courses
