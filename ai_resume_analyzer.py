import streamlit as st
import google.generativeai as genai

genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def analyze_resume(resume_text):

    prompt = f"""
    Analyze this resume:

    {resume_text}

    Provide:

    1. Strengths
    2. Weaknesses
    3. Suggestions for Improvement

    Keep it concise and professional.
    """

    response = model.generate_content(prompt)

    return response.text