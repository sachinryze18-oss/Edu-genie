"""Concept explanation using the local LaMini-Flan-T5-783M model.

Falls back to Gemini if the local model cannot be loaded (e.g. no torch installed).
"""
from gemini_client import ask_gemini

MODEL_ID = "MBZUAI/LaMini-Flan-T5-783M"
_pipe = None
_load_failed = False


def _get_pipeline():
    global _pipe, _load_failed
    if _pipe is None and not _load_failed:
        try:
            from transformers import pipeline
            _pipe = pipeline("text2text-generation", model=MODEL_ID)
        except Exception as e:  # missing deps, no internet on first run, etc.
            print(f"[EduGenie] Local model unavailable, using Gemini fallback: {e}")
            _load_failed = True
    return _pipe


def explain_concept(topic: str) -> str:
    pipe = _get_pipeline()
    if pipe is not None:
        prompt = f"Explain the following concept in simple words for a beginner: {topic}"
        out = pipe(prompt, max_length=300, do_sample=True, temperature=0.4)
        return out[0]["generated_text"].strip()
    try:
        return ask_gemini(f"Explain '{topic}' in simple words for a beginner, in under 150 words.")
    except Exception as e:
        return f"Error generating explanation: {e}"
