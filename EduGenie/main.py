"""EduGenie - Gemini powered learning assistant (FastAPI backend)."""
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from explanation_module import explain_concept
from learning_path import get_learning_recommendations
from qna import answer_question
from quiz_module import generate_quiz
from summary_module import summarize_text

app = FastAPI(title="EduGenie", description="Gemini powered learning assistant")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class TextInput(BaseModel):
    text: str


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.post("/qa")
async def qa(body: TextInput):
    return {"result": answer_question(body.text)}


@app.post("/explain")
async def explain(body: TextInput):
    return {"result": explain_concept(body.text)}


@app.post("/quiz")
async def quiz(body: TextInput):
    return {"result": generate_quiz(body.text)}


@app.post("/summarize")
async def summarize(body: TextInput):
    return {"result": summarize_text(body.text)}


@app.post("/learn/recommendations")
async def recommend(body: TextInput):
    return {"result": get_learning_recommendations(body.text)}
