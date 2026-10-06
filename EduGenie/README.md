# EduGenie – Gemini Powered Learning Assistant

FastAPI + HTML/CSS learning assistant: Q&A, concept explanation, quiz generation,
summarization and learning paths.

## Setup
```bash
python -m venv venv && source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env                                 # then put your Gemini API key in .env
uvicorn main:app --reload
```
Open http://127.0.0.1:8000

Get an API key at https://aistudio.google.com/apikey

## Endpoints (POST, JSON body `{"text": "..."}`)
| Endpoint | Module | Model |
|---|---|---|
| `/qa` | qna.py | Gemini |
| `/explain` | explanation_module.py | LaMini-Flan-T5-783M (local; Gemini fallback) |
| `/quiz` | quiz_module.py | Gemini (3 MCQs, JSON) |
| `/summarize` | summary_module.py | Gemini |
| `/learn/recommendations` | learning_path.py | Gemini |

## Notes
- First `/explain` call downloads the ~3 GB LaMini-Flan-T5 model from Hugging Face. If `torch`/`transformers` are missing or the download fails, it falls back to Gemini automatically.
- The document specifies Gemini 1.5 Pro, which Google has retired; the model is set via `GEMINI_MODEL` in `.env` (default `gemini-2.5-flash`).
- On Apple Silicon (M1), `pip install torch` works out of the box.
