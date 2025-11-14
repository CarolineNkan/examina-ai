import json

def grade_exam(user_answers_json, generated_questions_json):
    user_answers = json.loads(user_answers_json)
    gen = json.loads(generated_questions_json)

    score = 0
    details = []

    for i, q in enumerate(gen):
        correct = q["correct_answer"]
        user = user_answers.get(str(i), None)

        details.append({
            "question": q["question"],
            "correct": correct,
            "user": user,
            "explanation": q["explanation"],
            "is_correct": user == correct
        })

        if user == correct:
            score += 1

    return {
        "score": score,
        "total": len(gen),
        "details": details
    }
