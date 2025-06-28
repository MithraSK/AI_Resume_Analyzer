def match_keywords(resume_text, job_description):
    resume_words = set(resume_text.lower().split())
    job_keywords = set(job_description.lower().split())
    matched_keywords = resume_words.intersection(job_keywords)
    return matched_keywords
