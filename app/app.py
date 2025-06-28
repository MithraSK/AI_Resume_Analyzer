import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from src.resume_score import calculate_resume_score
from src.section_parser import parse_sections
from utils import get_text_from_file   # ✅ Fixed here

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")
st.title("🤖 AI Resume Analyzer")

resume_file = st.file_uploader("Upload your resume (PDF/DOCX)", type=["pdf", "docx"])
jd_input = st.text_area("Paste Job Description")

if resume_file and jd_input:
    resume_text = get_text_from_file(resume_file)
    score, matched = calculate_resume_score(resume_text, jd_input)
    sections = parse_sections(resume_text)

    st.markdown(f"### 🔍 Resume Score: **{score}%**")
    st.markdown("### ✅ Matched Keywords")
    st.write(", ".join(matched))

    st.markdown("### 📚 Resume Sections")
    for section, content in sections.items():
        st.markdown(f"#### {section.capitalize()}\\n{content}")
