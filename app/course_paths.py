"""Course path grouping for learner-facing pages."""
from __future__ import annotations

COURSE_PATHS = [
    {
        "id": "casual",
        "course_slugs": ("ai-fundamentals", "di-irankiai-kasdienai"),
    },
    {
        "id": "junior",
        "course_slugs": (
            "python-basics",
            "junior-ai-programuotojas",
            "build-ai-assistant",
            "applied-ai-engineering",
        ),
    },
]


def group_by_path(items: list[dict], *, course_key: str = "course") -> list[dict]:
    """Group card-like dicts by the configured learning paths."""
    by_slug = {item[course_key].slug: item for item in items}
    groups = []
    seen: set[str] = set()

    for path in COURSE_PATHS:
        path_items = []
        for slug in path["course_slugs"]:
            item = by_slug.get(slug)
            if item is not None:
                path_items.append(item)
                seen.add(slug)
        groups.append({"id": path["id"], "items": path_items})

    other_items = [
        item for item in items if item[course_key].slug not in seen
    ]
    if other_items:
        groups.append({"id": "other", "items": other_items})

    return groups
