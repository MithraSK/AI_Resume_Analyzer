from .keyword_matcher import match_keywords

def calculate_resume_score(resume_text, job_description):
    matched = match_keywords(resume_text, job_description)
    score = (len(matched) / len(set(job_description.split()))) * 100
    return round(score, 2), matched
