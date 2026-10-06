"""Shared Gemini helper used by qna, quiz, summary and learning-path modules."""
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
_client = None


def _get_client():
    global _client
    if _client is None:
        key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        if not key:
            raise RuntimeError("GEMINI_API_KEY is not set. Add it to your .env file.")
        _client = genai.Client(api_key=key)
    return _client


def ask_gemini(prompt: str) -> str:
    """Send a prompt to Gemini and return the text response."""
    response = _get_client().models.generate_content(model=MODEL_NAME, contents=prompt)
    text = getattr(response, "text", None)
    if not text:
        raise RuntimeError("Gemini returned an empty or blocked response.")
    return text.strip()
