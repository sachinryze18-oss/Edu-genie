"""Personalized learning path recommendations with Gemini."""
from gemini_client import ask_gemini


def get_learning_recommendations(topic: str) -> str:
    prompt = f"""Create a structured learning path for: {topic}

Organize it into Beginner, Intermediate and Advanced stages. For each stage give:
- Key concepts to learn
- Estimated time
- Recommended resources (videos, articles, books, practice sites)
- One small practice task

Finish with a short tip on how to stay consistent. Use clear headings and bullet points."""
    try:
        return ask_gemini(prompt)
    except Exception as e:
        return f"Error generating learning path: {e}"
