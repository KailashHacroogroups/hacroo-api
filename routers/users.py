from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Registeruser(BaseModel):
    name: str
    email: str

@router.post("/register")
def register_user(data: Registeruser):
    return {"status": "success", "message": f"User {data.name} registered"}
