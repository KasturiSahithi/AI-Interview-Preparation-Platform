import google.generativeai as genai
import streamlit as st

genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def evaluate_answer(questions, answers):

    try:

        prompt = f"""
        Interview Questions:

        {questions}

        Candidate Answers:

        {answers}

        Evaluate the overall interview performance.

        Return:

        Overall Score: X/10

        Strengths:
        - ...

        Weak Areas:
        - ...

        Question-wise Feedback:
        - Question 1: ...
        - Question 2: ...
        - Question 3: ...
        - Question 4: ...
        - Question 5: ...

        Final Recommendation:
        ...
        """

        response = model.generate_content(
            prompt
        )

        return response.text

    except Exception as e:

        return f"Error: {str(e)}"