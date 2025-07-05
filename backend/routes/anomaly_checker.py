from fastapi import APIRouter, UploadFile, File
import pandas as pd
import numpy as np

router = APIRouter(prefix="/anomaly", tags=["Anomaly Checker"])

@router.post("/")
async def check_anomalies(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)

    if "Zone" not in df.columns or "Usage" not in df.columns:
        return {"error": "CSV must contain 'Zone' and 'Usage' columns"}

    usage = df["Usage"]
    mean = usage.mean()
    std = usage.std()
    z_scores = (usage - mean) / std

    threshold = 2.0
    anomalies = df[z_scores.abs() > threshold]

    return {
        "anomalies": anomalies.to_dict(orient="records"),
        "threshold": threshold
    }
