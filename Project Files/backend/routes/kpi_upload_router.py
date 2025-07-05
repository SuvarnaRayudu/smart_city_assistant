from fastapi import APIRouter, UploadFile, File
import pandas as pd
from sklearn.linear_model import LinearRegression
from backend.models.kpi_model import KPIInput
import numpy as np

router = APIRouter(prefix="/kpi", tags=["KPI Forecasting"])

@router.post("/forecast")
async def forecast_kpi(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)

    if "Year" not in df.columns or "Value" not in df.columns:
        return {"error": "CSV must have 'Year' and 'Value' columns"}

    X = df["Year"].values.reshape(-1, 1)
    y = df["Value"].values

    model = LinearRegression()
    model.fit(X, y)

    next_year = np.max(X) + 1
    forecast = model.predict([[next_year]])

    return {
        "next_year": int(next_year),
        "forecast": float(forecast[0])
    }
