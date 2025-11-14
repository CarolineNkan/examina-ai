import os
from openai import OpenAI
from routes.search import expand_context

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_exam_questions(user_notes, num_q=10):
    """
    Generates exam questions based on user notes + expanded web context.
    """

    # Add web context from DuckDuckGo
    context = expand_context(user_notes)

    prompt = f"""
You are Examina, an AI exam-prep assistant.

Create **{num_q} high-quality exam questions** based on the student's notes.
Use the web context ONLY to clarify missing or unclear parts — not to override the notes.

=== STUDENT NOTES ===
{user_notes}

=== WEB CONTEXT ===
{context}

Requirements:
- Mix of multiple choice, short answer, and conceptual questions.
- Questions must be clear and varied.
- DO NOT include answers, only questions.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You generate exam-style questions."},
            {"role": "user", "content": prompt},
        ]
    )

    text = response.choices[0].message.content

    # Split into a list of questions
    questions = [q.strip() for q in text.split("\n") if q.strip()]

    return questions[:num_q]
