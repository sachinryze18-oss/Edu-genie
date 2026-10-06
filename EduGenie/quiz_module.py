"""Quiz generation: 3 MCQs with 4 options each, returned as parsed JSON."""
import json
import re
from gemini_client import ask_gemini


def clean_json_block(text: str) -> str:
    """Strip Markdown code fences (```json ... ```) around a JSON response."""
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    return text.strip()


def generate_quiz(passage: str):
    prompt = f"""You are a quiz generator for students.
Based on the topic or passage below, create exactly 3 multiple-choice questions.
Each question must have exactly 4 options and one correct answer.
Respond ONLY with valid JSON, no extra text, in this format:
[
  {{"question": "...", "options": ["A", "B", "C", "D"], "answer": "<must exactly match one option>"}}
]

Topic/Passage:
{passage}
"""
    try:
        raw = ask_gemini(prompt)
        data = json.loads(clean_json_block(raw))
        if not isinstance(data, list):
            raise ValueError("Quiz response was not a list")
        return data
    except Exception as e:
        return {"error": f"Failed to generate quiz: {e}"}
