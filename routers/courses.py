from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_courses():
    return [{"id": 1, "title": "AI for Cybersecurity"}, {"id": 2, "title": "Ethical Hacking 101"}]
