"""Sync markdown course content into the database.

Idempotent: run on every startup. Courses/lessons are upserted by slug,
and lessons no longer present in files are removed.
"""
from __future__ import annotations

from sqlalchemy import select

from app.content import load_courses
from app.database import SessionLocal
from app.models import Course, Lesson


def seed() -> None:
    courses = load_courses()
    db = SessionLocal()
    try:
        for c in courses:
            course = db.scalar(select(Course).where(Course.slug == c.slug))
            if course is None:
                course = Course(slug=c.slug)
                db.add(course)
            course.title = c.title
            course.description = c.description
            course.order = c.order
            db.flush()

            seen_slugs = set()
            for lf in c.lessons:
                seen_slugs.add(lf.slug)
                lesson = db.scalar(
                    select(Lesson).where(
                        Lesson.course_id == course.id, Lesson.slug == lf.slug
                    )
                )
                if lesson is None:
                    lesson = Lesson(course_id=course.id, slug=lf.slug)
                    db.add(lesson)
                lesson.title = lf.title
                lesson.module = lf.module
                lesson.content_md = lf.content_md
                lesson.order = lf.order

            # Remove lessons that no longer have a file.
            existing = db.scalars(
                select(Lesson).where(Lesson.course_id == course.id)
            ).all()
            for lesson in existing:
                if lesson.slug not in seen_slugs:
                    db.delete(lesson)

        db.commit()
        print(f"Seeded {len(courses)} courses.")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
