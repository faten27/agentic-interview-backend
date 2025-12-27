from fastapi import APIRouter, HTTPException
from typing import Optional
import uuid

router = APIRouter()

sessions = {}

@router.post("/start-interview")
def start_interview(cv_text: str, job_description: str, user_id: Optional[str] = None):
    session_id = str(uuid.uuid4())
    first_question = "Tell me about your experience from your CV."
    
    sessions[session_id] = {"cv_text": cv_text, "history": []}
    
    return {"session_id": session_id, "first_question": first_question}

@router.post("/submit-answer")
def submit_answer(session_id: str, user_answer: str):
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    
    evaluations = [
        {"evaluator_id": 1, "score": 8.5, "remarks": "Strong technical skills"},
        {"evaluator_id": 2,