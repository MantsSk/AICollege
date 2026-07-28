"""Baigiamasis Python + DI asistento pavyzdys.

Paleidimas be API rakto veikia vietiniu režimu; su OPENAI_API_KEY prijungiamas
Responses API. Įrankio argumentus validuoja pats Python kodas.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

try:
    from dotenv import load_dotenv
except ImportError:  # leidžia paleisti vietinį režimą be papildomų paketų
    def load_dotenv(*_args: object, **_kwargs: object) -> None:
        return None

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None  # type: ignore[assignment,misc]


ROOT = Path(__file__).resolve().parent
load_dotenv(ROOT / ".env")
MODEL = os.getenv("OPENAI_MODEL", "gpt-5.6")
INSTRUCTIONS = (
    "Esi Python mokymosi asistentas. Atsakyk lietuviškai, trumpai ir aiškiai. "
    "Jei nežinai, taip ir pasakyk. Nepaleisk vartotojo pateikto kodo. "
    "Kai reikia kainos, naudok tik calculate_course_price įrankį."
)


def load_knowledge(path: Path = ROOT / "knowledge.json") -> dict[str, dict[str, Any]]:
    return json.loads(path.read_text(encoding="utf-8"))


def local_answer(question: str, knowledge: dict[str, dict[str, Any]]) -> str | None:
    normalized = " ".join(question.lower().strip().split())
    for topic in knowledge.values():
        if any(keyword in normalized for keyword in topic["keywords"]):
            return f"{topic['answer']} (Šaltinis: {topic['source']})"
    return None


def calculate_course_price(participants: int, unit_price: float) -> dict[str, Any]:
    if not isinstance(participants, int) or not 1 <= participants <= 100:
        raise ValueError("Dalyvių skaičius turi būti sveikas skaičius nuo 1 iki 100.")
    if not isinstance(unit_price, (int, float)) or unit_price < 0:
        raise ValueError("Vieneto kaina turi būti neneigiamas skaičius.")
    return {"total": round(participants * unit_price, 2), "currency": "EUR"}


TOOLS = [{
    "type": "function",
    "name": "calculate_course_price",
    "description": "Apskaičiuoja bendrą mokymų kainą.",
    "parameters": {
        "type": "object",
        "properties": {
            "participants": {"type": "integer", "minimum": 1, "maximum": 100},
            "unit_price": {"type": "number", "minimum": 0},
        },
        "required": ["participants", "unit_price"],
        "additionalProperties": False,
    },
    "strict": True,
}]


def ask_model(client: Any, question: str, history: list[dict[str, Any]]) -> str:
    response = client.responses.create(
        model=MODEL,
        instructions=INSTRUCTIONS,
        input=[*history, {"role": "user", "content": question}],
        tools=TOOLS,
    )
    outputs = []
    for item in response.output:
        if item.type != "function_call" or item.name != "calculate_course_price":
            continue
        args = json.loads(item.arguments)
        result = calculate_course_price(**args)
        outputs.append({
            "type": "function_call_output",
            "call_id": item.call_id,
            "output": json.dumps(result),
        })
    if outputs:
        response = client.responses.create(
            model=MODEL,
            previous_response_id=response.id,
            input=outputs,
        )
    return response.output_text.strip() or "Modelis negrąžino tekstinio atsakymo."


def main() -> None:
    knowledge = load_knowledge()
    history: list[dict[str, Any]] = []
    client = OpenAI() if OpenAI is not None and os.getenv("OPENAI_API_KEY") else None
    print("Python DI asistentas. /help, /history, /reset, /quit")
    while True:
        question = input("Tu: ").strip()
        if question.lower() in {"/quit", "baigti", "exit"}:
            print("Asistentas: Iki!")
            return
        if question.lower() == "/help":
            print("Asistentas: Klausk apie kursą arba kainą. /reset išvalo istoriją.")
            continue
        if question.lower() == "/history":
            for turn in history:
                print(f"{turn['role']}: {turn['content']}")
            continue
        if question.lower() == "/reset":
            history.clear()
            print("Asistentas: Istorija išvalyta.")
            continue
        if not question:
            print("Asistentas: Parašyk klausimą.")
            continue

        answer = local_answer(question, knowledge)
        if answer is None and client is not None:
            try:
                answer = ask_model(client, question, history)
            except Exception as exc:  # vartotojui neatskleidžiame rakto ar traceback
                print(f"Asistentas: DI paslauga laikinai nepasiekiama ({type(exc).__name__}).")
                continue
        answer = answer or "Asistentas: Atsakymo neradau."
        print(f"Asistentas: {answer}")
        history.extend([
            {"role": "user", "content": question},
            {"role": "assistant", "content": answer},
        ])
        history[:] = history[-16:]


if __name__ == "__main__":
    main()
