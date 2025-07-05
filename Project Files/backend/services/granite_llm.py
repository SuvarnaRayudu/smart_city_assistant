import httpx
from backend.core.config import settings

# IBM Watsonx API endpoint
API_BASE_URL = "https://us-south.ml.cloud.ibm.com"

async def granite_generate(prompt: str):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {settings.watsonx_api_key}"
    }

    payload = {
        "model_id": settings.watsonx_model_id,
        "project_id": settings.watsonx_project_id,
        "input": prompt
    }

    async with httpx.AsyncClient() as client:
        res = await client.post(
            f"{API_BASE_URL}/ml/v1/text/generate",
            headers=headers,
            json=payload,
            timeout=30
        )

        if res.status_code == 200:
            return res.json()["results"][0]["generated_text"]
        else:
            return f"LLM Error: {res.text}"
