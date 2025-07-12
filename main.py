from fastapi import FastAPI
from routers import users, courses, tickets, feedback

app = FastAPI(title="Hacroo API")

app.include_router(users.router, prefix="/users")
app.include_router(courses.router, prefix="/courses")
app.include_router(tickets.router, prefix="/tickets")
app.include_router(feedback.router, prefix="/feedback")

@app.get("/")
def root():
    return {"message": "Welcome to Hacroo API - Phase 1"}
