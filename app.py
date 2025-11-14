from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

# Load .env before anything else
load_dotenv()

from routes.generate import generate_exam_questions
from routes.grade import grade_exam

app = Flask(__name__)


# ---------- ROUTES ----------

@app.route("/generate", methods=["POST"])
def generate_endpoint():
    data = request.get_json()
    notes = data.get("notes")
    num_q = data.get("num_q", 10)

    if not notes:
        return jsonify({"error": "Missing 'notes'"}), 400

    try:
        questions = generate_exam_questions(notes, num_q)
        return jsonify({"questions": questions})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/grade", methods=["POST"])
def grade_endpoint():
    data = request.get_json()
    answers = data.get("answers")

    if not answers:
        return jsonify({"error": "Missing 'answers'"}), 400

    try:
        result = grade_exam(answers)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ---------- MAIN ----------

if __name__ == "__main__":
    print("Loaded key:", os.getenv("OPENAI_API_KEY"))
    app.run(debug=True)
