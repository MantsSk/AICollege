"""AI Mentor — talks to any provider through LiteLLM.

The mentor is grounded in the current lesson (a focused, single-document
knowledge base) and instructed to prefer that content when answering.
"""
from __future__ import annotations

import os

from litellm import completion

from app.config import settings

# Make provider keys available to LiteLLM via the conventional env vars.
if settings.openai_api_key:
    os.environ.setdefault("OPENAI_API_KEY", settings.openai_api_key)
if settings.gemini_api_key:
    os.environ.setdefault("GEMINI_API_KEY", settings.gemini_api_key)
if settings.anthropic_api_key:
    os.environ.setdefault("ANTHROPIC_API_KEY", settings.anthropic_api_key)


SYSTEM_TEMPLATE = """You are the AI Mentor inside the "AI College" learning platform.

You are helping a student who is currently reading this lesson:

Course: {course_title}
Module: {module_title}
Lesson: {lesson_title}

Lesson content:
\"\"\"
{lesson_content}
\"\"\"

Your job:
- Prefer the lesson content above when answering. If the question goes beyond it, you may use general knowledge, but stay focused on learning.
- Explain concepts simply and clearly, as if to a motivated beginner.
- Generate small, concrete examples when helpful.
- Help debug code the student shares; point out the actual problem and how to fix it.
- Keep answers concise and friendly. Use markdown and code blocks.
- Stay on the topic of learning programming and AI. Politely redirect off-topic questions.
"""

MAX_HISTORY_MESSAGES = 12


def build_messages(
    *,
    course_title: str,
    module_title: str,
    lesson_title: str,
    lesson_content: str,
    history: list[dict[str, str]],
    user_message: str,
) -> list[dict[str, str]]:
    system = SYSTEM_TEMPLATE.format(
        course_title=course_title,
        module_title=module_title or "—",
        lesson_title=lesson_title,
        lesson_content=lesson_content[:8000],
    )
    messages = [{"role": "system", "content": system}]
    messages.extend(history[-MAX_HISTORY_MESSAGES:])
    messages.append({"role": "user", "content": user_message})
    return messages


def ask_mentor(messages: list[dict[str, str]]) -> str:
    """Send messages to the configured model and return the reply text."""
    try:
        response = completion(
            model=settings.ai_model,
            messages=messages,
            temperature=settings.ai_temperature,
            max_tokens=settings.ai_max_tokens,
        )
        return response.choices[0].message.content or ""
    except Exception as exc:  # noqa: BLE001 — surface a friendly message to the user
        if settings.debug:
            return f"⚠️ The AI Mentor is unavailable right now (`{exc}`). Check your AI_MODEL and API key configuration."
        return "⚠️ The AI Mentor is temporarily unavailable. Please try again in a moment."
