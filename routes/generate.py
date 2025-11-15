import os
from openai import OpenAI
from routes.search import expand_context

# Load API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_exam_questions(user_notes, num_q=10):
    """
    Generate exam questions using GPT-4o-mini + DuckDuckGo context.
    """

    context = expand_context(user_notes)

    prompt = f"""
You are EXAMINA, an AI exam-prep assistant.

Create **{num_q} high-quality exam questions** based ONLY on the user's notes.
Use web context as a helper, not the main source.

=== NOTES ===
{user_notes}

=== WEB CONTEXT ===
{context}

Rules:
- Mix multiple choice, short answer, and applied/conceptual questions.
- DO NOT include answers.
- Number each question clearly.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You generate exam-style questions only."},
            {"role": "user", "content": prompt}
        ]
    )

    text = response.choices[0].message.content
    questions = [q.strip() for q in text.split("\n") if q.strip()]

    return questions[:num_q]
