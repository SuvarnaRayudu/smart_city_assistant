from fastapi import APIRouter, Query
from backend.services.granite_llm import granite_generate

router = APIRouter(prefix="/eco", tags=["Eco Tips"])

@router.get("/tips")
async def get_eco_tips(topic: str = Query(...)):
    prompt = f"Give 5 actionable eco-friendly tips related to {topic}."
    tips = await granite_generate(prompt)
    return {"tips": tips}
