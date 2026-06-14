import google.generativeai as genai
import streamlit as st

genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def generate_questions(resume_text, difficulty):

    try:

        prompt = f"""
Analyze the following resume:

{resume_text}

Generate interview questions based on:
DO NOT provide:
- Resume analysis
- Strengths
- Weaknesses
- Suggestions
- Explanations

Create:

Easy Questions (5)
Medium Questions (5)
Hard Questions (5)

Rules:

- Questions must be based on the resume
- Questions must be technical
- Questions must be project-based
- Questions must be interview style
- Number all questions

Format exactly like:

EASY:
1.
2.
3.
4.
5.

MEDIUM:
1.
2.
3.
4.
5.

HARD:
1.
2.
3.
4.
5.
"""

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        return f"ERROR: {str(e)}"