from pydantic import BaseModel

class KPIInput(BaseModel):
    year: int
    value: float
