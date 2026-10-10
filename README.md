# AI Study Assistant Chatbot Using Generative AI (Google Gemini)

A web-based study chatbot built with **Python, Streamlit and Google Gemini**.
A student types a study question and gets a clear, generated answer in one of three styles:
**Simple**, **Exam-oriented** or **Example-based**.

**Author:** Anagandula Shivani (236F1A6703), CSE (Data Science)
**College:** Pallavi Engineering College | **Academic Year:** 2026-2027
**Guide:** Mr. Raghavendra Roa

## Features
- Generative AI answers using the Google Gemini API
- Three answer styles (prompt engineering)
- Chat memory for follow-up questions
- Input validation and fallback models for error handling
- API key entered in the sidebar (never stored in the code)

## Tech Stack
Python 3.13 | Streamlit | google-genai (Google GenAI Python SDK)

## How to Run
1. Install the libraries:
   ```
   pip install -r requirements.txt
   ```
2. Get a free API key from [Google AI Studio](https://aistudio.google.com).
3. Start the app:
   ```
   python -m streamlit run ai_study_assistant.py
   ```
4. Open `http://localhost:8501`, paste your API key in the left sidebar and ask a question,
   for example: `What is machine learning?`

## How It Works
1. The user types a question in the chat box.
2. The question is combined with a system prompt and the selected answer style.
3. The prompt is sent to the Gemini model through the API.
4. The generated answer is shown in the chat window.

## Screenshots
Application screenshots (home page, question input, exam-style answer and simple-style answer) are included in this repository as PNG files.

## Note
Never upload or share your API key. Each user enters their own key in the app.
