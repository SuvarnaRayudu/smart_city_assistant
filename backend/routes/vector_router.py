from fastapi import APIRouter, UploadFile, File, Query
from backend.services.document_embedder import embed_and_store
from backend.services.document_retriever import search_policies
from backend.models.policy_model import PolicySearchRequest

router = APIRouter(prefix="/vector", tags=["Vector Search"])

@router.post("/upload")
async def upload_and_embed(document_id: str = Query(...), file: UploadFile = File(...)):
    text = (await file.read()).decode("utf-8")
    return embed_and_store(document_id, text)

@router.get("/search")
async def semantic_search(query: str):
    results = search_policies(query)
    return {"results": results}
