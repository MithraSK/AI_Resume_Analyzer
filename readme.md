# 🤖 AI Resume Analyzer

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live--App-ff4b4b?logo=streamlit)](#)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An AI-powered Resume Analyzer built using Python and Streamlit that evaluates resumes against job descriptions, highlights matched keywords, and gives a resume match score.

---

## 📂 Project Structure

AI_Resume_Analyzer/

│

├── app/

│ ├── app.py # Streamlit frontend

│ └── utils.py # File handling

│

├── src/

│ ├── extract_text.py # PDF/DOCX text extractor

│ ├── keyword_matcher.py # Keyword matching logic

│ ├── resume_score.py # Resume scoring

│ └── section_parser.py # Section extraction (skills, education, etc.)

│


├── data/

│ ├── sample_resumes/ # Test resumes

│ └── job_descriptions/ # Sample job descriptions

│

├── requirements.txt

└── README.md

y

---

## 🔍 Features

- 📄 Upload PDF or DOCX resumes  
- 📋 Paste any job description  
- 🔍 Extracts keywords & resume sections  
- 📈 Calculates resume match score  
- ⚡ Instant feedback with Streamlit interface

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/MithraSK/AI_Resume_Analyzer.git
cd AI_Resume_Analyzer
2. Install dependencies


pip install -r requirements.txt

3. Run the app


streamlit run app/app.py

---

You can test using files inside the data/ folder:


📄 Sample resume: data/sample_resumes/sample_resume.docx


📝 Job description: data/job_descriptions/data_analyst.txt


---

📌 To-Do
 
*Streamlit Cloud Deployment

 
*Improve section parsing with NLP

 
*Add resume score visualization

 
*Add email parsing, contact info, etc.

.

📄 License

This project is licensed under the MIT License.


---

Author:
Mithra S K

📧 [mithrask46@gmail.com]

🌐 [github.com/MithraSK]

