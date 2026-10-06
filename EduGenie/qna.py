"""Question answering with Gemini."""
from gemini_client import ask_gemini


def answer_question(question: str) -> str:
    prompt = (
        "You are EduGenie, a friendly educational assistant. Answer the student's "
        "question accurately and concisely (2-5 sentences unless more is needed).\n\n"
        f"Question: {question}"
    )
    try:
        return ask_gemini(prompt)
    except Exception as e:
        return f"Error generating answer: {e}"
