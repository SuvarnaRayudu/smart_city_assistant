from fastapi import APIRouter
from pydantic import BaseModel
from backend.models.chat_model import ChatInput
from backend.services.granite_llm import granite_generate

router = APIRouter(prefix="/chat", tags=["Chat Assistant"])

class ChatInput(BaseModel):
    prompt: str

@router.post("/")
async def chat_endpoint(data: ChatInput):
    response = await granite_generate(data.prompt)
    return {"response": response}
