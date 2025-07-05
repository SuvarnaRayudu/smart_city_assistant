from fastapi import FastAPI
from backend.routes import vector_router
from backend.routes import (
    chat_router, feedback_router, eco_tips_router,
    kpi_upload_router, anomaly_checker, summarizer_router
)

app = FastAPI(title="Sustainable Smart City Assistant")

app.include_router(chat_router.router)
app.include_router(feedback_router.router)
app.include_router(eco_tips_router.router)
app.include_router(kpi_upload_router.router)
app.include_router(anomaly_checker.router)
app.include_router(summarizer_router.router)

app.include_router(vector_router.router)

@app.get("/")
def root():
    return {"message": "Smart City Assistant backend is up"}
