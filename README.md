# 🎯 AI Interview Preparation Platform

An AI-powered Interview Preparation Platform built using Python, Streamlit, and Google Gemini AI. The platform helps users analyze resumes, calculate ATS scores, generate interview questions, evaluate answers, and download detailed PDF reports.

## 🚀 Live Demo

🔗 Deployed Streamlit URL 

https://ai-interview-preparation-platform.streamlit.app/

---

## 📌 Features

### 📄 Resume Upload & Analysis
- Upload resumes in PDF format
- Extract resume content automatically
- AI-powered resume analysis using Gemini AI

### ✅ Skill Detection
- Detects technical skills from uploaded resumes
- Displays identified skills instantly

### 🏆 Resume Score
- Calculates a resume quality score based on:
  - Skills
  - Projects
  - Education
  - Certifications
  - Experience

### 📈 ATS Score
- Estimates Applicant Tracking System (ATS) compatibility
- Evaluates resume structure and important sections

### 🚀 Career Recommendations
- Recommends suitable career paths based on detected skills
- Includes descriptions for each recommended role

### 🤖 AI Interview Question Generator
- Generates interview questions using Gemini AI
- Supports:
  - Easy
  - Medium
  - Hard

### 🎤 AI Mock Interview
- Allows users to answer generated questions
- AI evaluates responses and provides:
  - Score
  - Strengths
  - Areas for Improvement
  - Final Feedback

### 📄 PDF Report Generation
- Generates downloadable interview reports
- Includes:
  - Resume Score
  - ATS Score
  - Skills
  - Career Recommendations
  - Questions
  - AI Feedback

---

## 🛠️ Technologies Used

### Frontend
- Streamlit

### Backend
- Python

### AI
- Google Gemini API

### Libraries
- Streamlit
- Google Generative AI
- PyPDF2
- ReportLab
- Pandas
- Plotly

---

## 📂 Project Structure

```text
AI-Interview-Preparation-Platform/
│
├── app.py
├── ai_resume_analyzer.py
├── ai_question_generator.py
├── ai_answer_evaluator.py
├── pdf_generator.py
├── requirements.txt
│
└── data/
    └── skills.py
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/KasturiSahithi/AI-Interview-Preparation-Platform.git

```

### Navigate to Project

```bash
cd AI-Interview-Preparation-Platform
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create Secrets File

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
```

### Run Application

```bash
streamlit run app.py
```

---

## 🎯 Future Enhancements

- Interview History Tracking
- User Authentication
- Resume Improvement Suggestions
- AI Voice-Based Mock Interviews
- Job Role Specific Question Generation
- Performance Analytics Dashboard

---

## 👩‍💻 Author

**Kasturi Sahithi**

B.Tech Electrical and Electronics Engineering (EEE)
kasturisahithi068@gmail.com

---

## 📜 License

This project is developed for educational and portfolio purposes.
