"""Summarization with Gemini."""
from gemini_client import ask_gemini


def summarize_text(text: str) -> str:
    prompt = (
        "Summarize the following educational passage into a concise, easy-to-understand "
        "summary for quick revision. Keep the key points and remove redundancy. "
        "Use short bullet points where helpful.\n\n"
        f"{text}"
    )
    try:
        return ask_gemini(prompt)
    except Exception as e:
        return f"Error generating summary: {e}"
