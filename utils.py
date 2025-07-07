# utils.py
def format_prompt(profile, scholarships):
    prompt = f"""Based on the following user profile:\n\n{profile}\n\nAnd available scholarships:\n"""
    for s in scholarships:
        prompt += f"- {s['title']}: {s['url']}\n"
    prompt += "\nRecommend the top scholarships with reasons."
    return prompt
