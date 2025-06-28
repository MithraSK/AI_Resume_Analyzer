import re

def parse_sections(text):
    sections = {}
    text = text.lower()

    patterns = {
        'education': r'(education|academic background)(.*?)(?=experience|skills|projects|$)',
        'experience': r'(experience|work history)(.*?)(?=education|skills|projects|$)',
        'skills': r'(skills|technical skills)(.*?)(?=experience|education|projects|$)',
    }

    for section, pattern in patterns.items():
        match = re.search(pattern, text, re.DOTALL)
        if match:
            sections[section] = match.group(2).strip()
        else:
            sections[section] = 'Not Found'

    return sections
