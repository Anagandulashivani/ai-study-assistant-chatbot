"""
AI Study Assistant Chatbot Using Generative AI (Google Gemini)

Name   : ANAGANDULA SHIVANI
Roll No: 236F1A6703
Branch : CSE (Data Science)

Install:
    pip install streamlit google-genai

Run:
    python -m streamlit run ai_study_assistant.py
"""

import streamlit as st
from google import genai
from google.genai import types

# If one model name is not available, the next one is tried automatically.
MODELS = ["gemini-3.8-flash", "gemini-3.5-flash", "gemini-2.5-flash"]

# Prompt engineering: each answer style has its own instruction.
STYLES = {
    "Simple (beginner friendly)": "Explain in very simple words with one easy example.",
    "Exam-oriented (semester level)": "Give a definition, 4 to 5 key points, and a short conclusion, as written in a semester exam.",
    "Example-based": "Explain the concept using two real-life examples.",
}

SYSTEM_PROMPT = (
    "You are a friendly AI Study Assistant for college students. "
    "Answer only study-related questions about subjects like AI, Data Science, "
    "Python and Computer Science. Keep answers clear, correct and under 200 words. "
    "If the question is not study-related, politely say you can only help with studies."
)

st.set_page_config(page_title="AI Study Assistant", page_icon="📘")
st.title("📘 AI Study Assistant")
st.caption("A Generative AI chatbot built with Python, Streamlit and Google Gemini")

# Sidebar: API key and answer style
api_key = st.sidebar.text_input("Gemini API Key", type="password")
style = st.sidebar.selectbox("Answer style", list(STYLES.keys()))
if st.sidebar.button("Clear chat"):
    st.session_state.messages = []

if "messages" not in st.session_state:
    st.session_state.messages = []

# Show old messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["text"])


def ask_gemini(question):
    """Build the prompt, call the GenAI model, and return the answer text."""
    client = genai.Client(api_key=api_key)
    history = "\n".join(f"{m['role']}: {m['text']}" for m in st.session_state.messages[-6:])
    prompt = f"{STYLES[style]}\n\nPrevious chat:\n{history}\n\nQuestion: {question}"
    config = types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT, temperature=0.5)

    last_error = None
    for model in MODELS:
        try:
            response = client.models.generate_content(model=model, contents=prompt, config=config)
            return response.text
        except Exception as error:  # fallback handling
            if last_error is None:
                last_error = error  # remember the first (real) error
    return f"Sorry, the AI service is not available right now. Details: {last_error}"


question = st.chat_input("Ask a study question, e.g. What is machine learning?")

if question:
    question = question.strip()[:500]  # input validation: limit the length
    if not api_key:
        st.warning("Please enter your Gemini API key in the left sidebar first.")
    else:
        with st.chat_message("user"):
            st.write(question)
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                answer = ask_gemini(question)
            st.write(answer)
        st.session_state.messages.append({"role": "user", "text": question})
        st.session_state.messages.append({"role": "assistant", "text": answer})
