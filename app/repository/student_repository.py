from sqlalchemy.ext.asyncio import AsyncSession 
from app.schemas.student_schema import Register , Login
from app.models.students_model import Student
from sqlalchemy import select



async def register_student(db:AsyncSession , student:Register):
    db.add(student)
    await db.commit()
    await db.refresh(student)
    return student

async def check_email(email_id:str , db:AsyncSession):
    check=await db.execute(select(Student).where(Student.email==email_id))
    return check.scalar_one_or_none()

async def login_student(db:AsyncSession , email:str):
    result=await db.execute(select(Student).where(Student.email==email))
    return result.scalar_one_or_none()