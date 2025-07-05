from pydantic import BaseModel

class Feedback(BaseModel):
    name: str
    category: str
    message: str
