from fastapi import APIRouter, UploadFile, File
from backend.services.granite_llm import granite_generate

router = APIRouter(prefix="/policy", tags=["Policy Summarizer"])

@router.post("/summarize")
async def summarize_policy(file: UploadFile = File(...)):
    content = (await file.read()).decode("utf-8")
    prompt = f"Summarize this policy document in simple terms:\n\n{content}"
    summary = await granite_generate(prompt)
    return {"summary": summary}
