from fastapi import FastAPI

app = FastAPI(title="Agentic Interview Council API")

@app.get("/")
def home():
    return {"message": "Hello! Backend is running."}

@app.get("/test")
def test():
    return {"status": "Working!"}

@app.post("/start-interview")
def start_interview(cv_text: str, job_description: str):
    return {"session_id": "12345", "first_question": "Tell me about yourself."}

@app.post("/submit-answer")
def submit_answer(session_id: str, user_answer: str):
    return {
        "next_question": "What is your biggest achievement?",
        "evaluations": [
            {"evaluator_id": 1, "score": 8.5, "remarks": "Good"},
            {"evaluator_id": 2, "score": 8.0, "remarks": "Clear"},
            {"evaluator_id": 3, "score": 9.0, "remarks": "Excellent"},
            {"evaluator_id": 4, "score": 8.2, "remarks": "Strong"}
        ],
        "overall_score": 8.4,
        "coach_advice": "Great job!"
    }
