import os
import streamlit as st
from PyPDF2 import PdfReader
from pdf_generator import generate_pdf
from ai_resume_analyzer import analyze_resume
from data.skills import SKILLS_DATABASE
from ai_answer_evaluator import evaluate_answer
from ai_question_generator import generate_questions
import sqlite3
# ----------------------------
# DATABASE SETUP
# ----------------------------
conn = sqlite3.connect(
    "interview_history.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS interviews (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    score INTEGER,

    total_questions INTEGER,

    resume_score INTEGER
)
""")
conn.commit()
st.set_page_config(
    page_title="AI Interview Preparation Platform",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 AI Interview Preparation Platform")

uploaded_file = st.file_uploader(
    "Upload Your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    pdf_reader = PdfReader(uploaded_file)

    text = ""

    for page in pdf_reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text

    st.subheader("📄 Resume Content")

    st.text_area(
        "Extracted Text",
        text,
        height=250
    )
    st.subheader("📊 AI Resume Analysis")

    if st.button("Analyze Resume"):
        with st.spinner("🔍 Analyzing Resume..."):
           analysis = analyze_resume(text)

        st.write(analysis)
   
    # ----------------------------
    # SKILL DETECTION
    # ----------------------------

    detected_skills = []

    for skill in SKILLS_DATABASE:

        if skill.lower() in text.lower():

            detected_skills.append(skill)

    st.subheader("✅ Detected Skills")

    if detected_skills:

        for skill in detected_skills:

            st.success(skill)

    else:

        st.warning("No skills detected")

    # ----------------------------
    # RESUME SCORE
    # ----------------------------

    st.subheader("🏆 Resume Score")

    resume_score = 0

# Skills
    resume_score += min(len(detected_skills) * 2, 30)

# Projects
    if "project" in text.lower():
       resume_score += 15

# Education
    if "education" in text.lower():
       resume_score += 10

# Contact Info
    if "@" in text:
       resume_score += 10

# Certifications
    if (
    "certificate" in text.lower()
    or
    "certification" in text.lower()
    ):
       resume_score += 10

# Internship / Experience
    if (
    "internship" in text.lower()
    or
    "experience" in text.lower()
    ):
       resume_score += 10

    resume_score = min(resume_score, 100)

    st.progress(resume_score / 100)

    st.success(
        f"Resume Score: {resume_score}/100"
    )
    # ATS SCORE

    ats_score = 0

    if "@" in text:
       ats_score += 15

    if len(detected_skills) >= 5:
        ats_score += 10

    if "project" in text.lower():
        ats_score += 15

    if "education" in text.lower():
        ats_score += 15

    if (
    "linkedin" in text.lower()
    or
    "github" in text.lower()
    ):
       ats_score += 15
    # Internship / Experience
    if (
    "internship" in text.lower()
    or
    "experience" in text.lower()
    ):
       ats_score += 20

    ats_score = min(ats_score, 100)

    st.subheader("📈 ATS Score")

    st.progress(ats_score / 100)

    st.info(
    f"ATS Score: {ats_score}/100"
    )

# ----------------------------
# CAREER RECOMMENDATIONS
# ----------------------------

    st.subheader("🚀 Recommended Career Paths")

    career_mapping = {

    "Python": [
        "Software Developer",
        "Data Analyst",
        "Data Scientist"
    ],

    "SQL": [
        "Data Analyst",
        "Database Developer"
    ],

    "Power BI": [
        "Business Intelligence Analyst",
        "Data Analyst"
    ],

    "Tableau": [
        "Data Analyst",
        "Business Intelligence Analyst"
    ],

    "Machine Learning": [
        "Data Scientist",
        "ML Engineer"
    ],

    "TensorFlow": [
        "AI Engineer",
        "ML Engineer"
    ],

    "PyTorch": [
        "AI Engineer",
        "ML Engineer"
    ],

    "HTML": [
        "Web Developer"
    ],

    "CSS": [
        "Web Developer"
    ],

    "React": [
        "Frontend Developer"
    ],

    "Django": [
        "Backend Developer",
        "Full Stack Developer"
    ],

    "AWS": [
        "Cloud Engineer"
    ],

    "Azure": [
        "Cloud Engineer"
    ],

    "VLSI": [
        "VLSI Engineer"
    ],

    "FPGA": [
        "VLSI Engineer"
    ],

    "Verilog": [
        "VLSI Engineer"
    ],

    "Arduino": [
        "Embedded Systems Engineer"
    ],

    "ESP32": [
        "IoT Engineer",
        "Embedded Systems Engineer"
    ],

    "Power Systems": [
        "Electrical Engineer"
    ],

    "Electrical Machines": [
        "Electrical Engineer"
    ]
}

    career_descriptions = {

    "Data Analyst":
    "Analyze data, build dashboards and generate business insights.",

    "Data Scientist":
    "Build machine learning models and predictive solutions.",

    "Software Developer":
    "Design and develop software applications and systems.",

    "Database Developer":
    "Design, optimize and maintain databases.",

    "Business Intelligence Analyst":
    "Create reports, dashboards and business analytics solutions.",

    "Web Developer":
    "Develop responsive websites and web applications.",

    "Frontend Developer":
    "Build interactive user interfaces.",

    "Backend Developer":
    "Develop APIs and server-side applications.",

    "Full Stack Developer":
    "Work on both frontend and backend systems.",

    "Cloud Engineer":
    "Design and manage cloud infrastructure.",

    "AI Engineer":
    "Build AI-powered applications and systems.",

    "ML Engineer":
    "Deploy and maintain machine learning models.",

    "VLSI Engineer":
    "Design integrated circuits and semiconductor systems.",

    "Embedded Systems Engineer":
    "Develop hardware-software integrated systems.",

    "IoT Engineer":
    "Build connected smart devices and IoT solutions.",

    "Electrical Engineer":
    "Work on power systems, machines and electrical design."
}

    career_paths = []

    for skill in detected_skills:

      if skill in career_mapping:

            career_paths.extend(
                career_mapping[skill]
            )

    career_paths = list(set(career_paths))

    if career_paths:

        for career in career_paths:

            st.success(career)

            st.caption(
               career_descriptions.get(
                career,
                ""
               )
           )

    else:

         st.info(
        "No career recommendations found."
         )
        
# ----------------------------
# AI QUESTIONS
# ----------------------------

    st.subheader("🤖 AI Generated Interview Questions")
    difficulty = st.selectbox(
    "Select Interview Difficulty",
    ["Easy", "Medium", "Hard"]
    )

    if "questions" not in st.session_state:
       st.session_state.questions = ""

    if st.button("Generate AI Questions"):
       with st.spinner("🤖 Generating Questions..."):
         st.session_state.questions = generate_questions(
        text,
        difficulty
    )

    questions = st.session_state.questions

    if questions:

       selected_level = st.selectbox(
        "Select Question Difficulty",
        ["Easy", "Medium", "Hard"]
       )

       display_questions = questions

       if selected_level == "Easy":

          if "MEDIUM:" in questions:

              display_questions = questions.split(
                "MEDIUM:"
              )[0]

       elif selected_level == "Medium":

         if (
            "MEDIUM:" in questions
            and
            "HARD:" in questions
         ):

            display_questions = questions.split(
                "MEDIUM:"
            )[1].split(
                "HARD:"
            )[0]

       elif selected_level == "Hard":

           if "HARD:" in questions:

               display_questions = questions.split(
                "HARD:"
               )[1]

       question_lines = display_questions.split("\n")

       questions_list = []

       for line in question_lines:

            line = line.strip()

            if any(
                line.startswith(f"{i}.")
                for i in range(1, 11)
            ):


               questions_list.append(line)

       for i, question in enumerate(questions_list):

            st.markdown(f"**{question}**")

            st.text_area(
            "Your Answer",
            key=f"answer_{selected_level}_{i}"
             )

   
    # ----------------------------
    # AI MOCK INTERVIEW
    # ----------------------------

    st.subheader("🎤 AI Mock Interview")
    if not questions:

        st.warning("Please generate questions first.")

    else:

      if st.button("Evaluate All Answers"):

        all_answers = ""

        for i in range(len(questions_list)):

            answer = st.session_state.get(
                f"answer_{selected_level}_{i}",
                ""
            )

            all_answers += f"""
Question {i+1} Answer:

{answer}

"""

        if all_answers.strip() == "":

            st.warning(
                "Please answer at least one question."
            )

        else:

            feedback = evaluate_answer(
                display_questions,
                all_answers
            )

            st.subheader("🤖 AI Feedback")

            st.write(feedback)
            pdf_file = generate_pdf(
              "Interview_Report.pdf",
               resume_score,
               detected_skills,
               career_paths,
               analysis if 'analysis' in locals() else "",
               display_questions,
               feedback
            )

            with open(pdf_file, "rb") as file:

                st.download_button(
        label="📄 Download Interview Report",
        data=file,
        file_name="Interview_Report.pdf",
        mime="application/pdf"
                )