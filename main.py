from fastapi import FastAPI

app = FastAPI(title="Agentic Interview Council API")

@app.get("/")
def home():
    return {"message": "Agentic Interview Backend is running! Check the POST endpoints below."}

@app.get("/test")
def test():
    return {"status": "Test endpoint working!"}

@app.post("/start-interview")
def start_interview(cv_text: str, job_description: str):
    return {
        "session_id": "demo-session-12345",
        "first_question": "Tell me about yourself and your background from your CV."
    }

@app.post("/submit-answer")
def submit_answer(session_id: str, user_answer: str):
    return {
        "next_question": "What is your experience with Python and FastAPI?",
        "evaluations": [
            {"evaluator_id": 1, "score": 8.5, "remarks": "Strong technical knowledge"},
            {"evaluator_id": 2, "score": 8.0, "remarks": "Good structure in answer"},
            {"evaluator_id": 3, "score": 9.0, "remarks": "Excellent examples"},
            {"evaluator_id": 4, "score": 8.2, "remarks": "Confident and clear"}
        ],
        "overall_score": 8.4,
        "coach_advice": "Great job! Try to add more specific metrics next time.",
        "interview_ended": False
    }
