from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Feedback(BaseModel):
    name: str
    email: str

@router.post("/register")
def register_user(data: Feedback):
    return {"status": "success", "message": f"User {data.name} registered"}
