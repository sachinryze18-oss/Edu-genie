"""EduGenie – Streamlit demo. Run with:  streamlit run streamlit_app.py"""
import streamlit as st

from explanation_module import explain_concept
from learning_path import get_learning_recommendations
from qna import answer_question
from quiz_module import generate_quiz
from summary_module import summarize_text

st.set_page_config(page_title="EduGenie", page_icon="🎓", layout="centered")

TASKS = {
    "💬 Ask a Question": ("qa", "Which is the largest ocean?", answer_question),
    "💡 Explain a Concept": ("explain", "Photosynthesis", explain_concept),
    "📝 Generate Quiz": ("quiz", "Pythagoras Theorem (or paste a passage)", generate_quiz),
    "📄 Summarize Text": ("summarize", "Paste a long paragraph here...", summarize_text),
    "🗺️ Learning Path": ("recommend", "SQL", get_learning_recommendations),
}

st.title("🎓 EduGenie")
st.caption("Gemini-powered learning assistant")

with st.sidebar:
    st.header("Choose a task")
    label = st.radio("Task", list(TASKS), label_visibility="collapsed")
    st.divider()
    st.markdown("**Scenarios to try**")
    st.markdown("- *Which is the largest ocean?*\n- Quiz on *Pythagoras Theorem*\n- Learning path for *SQL*")

key, placeholder, func = TASKS[label]
text = st.text_area("Your input", placeholder=placeholder, height=150, key=f"input_{key}")

if st.button("Submit", type="primary", use_container_width=True):
    if not text.strip():
        st.warning("Please enter some text first.")
    else:
        with st.spinner("Thinking..."):
            st.session_state[f"result_{key}"] = func(text.strip())
        # reset any previous quiz answers
        for k in [k for k in st.session_state if k.startswith("quiz_q")]:
            del st.session_state[k]

result = st.session_state.get(f"result_{key}")

if result is not None:
    st.divider()
    if key == "quiz":
        if isinstance(result, dict) and "error" in result:
            st.error(result["error"])
        else:
            st.subheader("Quiz")
            score, answered = 0, 0
            for i, q in enumerate(result):
                choice = st.radio(
                    f"**Q{i + 1}. {q['question']}**", q["options"],
                    index=None, key=f"quiz_q{i}",
                )
                if choice is not None:
                    answered += 1
                    if choice == q["answer"]:
                        score += 1
                        st.success("✅ Correct!")
                    else:
                        st.error(f"❌ Incorrect. The correct answer is: {q['answer']}")
            if answered == len(result):
                st.metric("Your score", f"{score} / {len(result)}")
                if score == len(result):
                    st.balloons()
    else:
        st.subheader("Result")
        st.markdown(result)
