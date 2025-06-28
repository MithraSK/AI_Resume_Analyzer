import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.extract_text import extract_text_from_pdf, extract_text_from_docx

def get_text_from_file(file):
    temp_path = os.path.join("temp", file.name)
    os.makedirs("temp", exist_ok=True)

    with open(temp_path, "wb") as f:
        f.write(file.read())

    if file.name.endswith(".pdf"):
        return extract_text_from_pdf(temp_path)
    elif file.name.endswith(".docx"):
        return extract_text_from_docx(temp_path)
    else:
        return "Unsupported file format. Please upload PDF or DOCX."
