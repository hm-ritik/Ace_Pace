from fastapi import FastAPI 
from app.routes.students_routes import router as student_router
from app.core.database import engine, Base
from app.models.students_model import Student
from app.routes.file_route import router as file_router



app=FastAPI(title="Ace Pace")
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten this to your Streamlit URL once deployed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(student_router, prefix="/students", tags=["Students"])
app.include_router(file_router, prefix="/files", tags=["Files"])

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/home")


def home():
    return{
        "Message": "Checking Server"
    }