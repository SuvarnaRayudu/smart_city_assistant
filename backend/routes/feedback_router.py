from fastapi import APIRouter
from backend.models.feedback_model import Feedback
from pydantic import BaseModel
import json
from datetime import datetime
import os

router = APIRouter(prefix="/feedback", tags=["Citizen Feedback"])

FEEDBACK_PATH = "data/feedbacks/feedback.json"

class Feedback(BaseModel):
    name: str
    category: str
    message: str

@router.post("/")
def submit_feedback(data: Feedback):
    feedback_entry = {
        "name": data.name,
        "category": data.category,
        "message": data.message,
        "timestamp": datetime.now().isoformat()
    }

    os.makedirs(os.path.dirname(FEEDBACK_PATH), exist_ok=True)

    if os.path.exists(FEEDBACK_PATH):
        with open(FEEDBACK_PATH, "r") as f:
            feedback_data = json.load(f)
    else:
        feedback_data = []

    feedback_data.append(feedback_entry)

    with open(FEEDBACK_PATH, "w") as f:
        json.dump(feedback_data, f, indent=4)

    return {"message": "Feedback submitted successfully "}
