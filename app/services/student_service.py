from app.repository.student_repository import login_student , register_student
from app.schemas.student_schema import Register , Login 
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.students_model import Student
from fastapi import HTTPException
from app.core.security import hash_password , verify_password
from app.repository.student_repository import register_student , check_email

""" name:str = Field(min_length=2 , max_length=25)
    email: EmailStr
    hashed_password:str = Field(min_length=6 , max_length=8)"""


def register_user(post:Register , db:AsyncSession , current_user:Student):
    if current_user.role != 'Admin':
        raise HTTPException(status_code=403 , detail="Not Allowed")
    existing_user=check_email(post.email , db)
    if existing_user:
        raise HTTPException(status_code=400 , detail="User Already Exists")
    hashed_password=hash_password(post.password)
    user=Student(
         name=post.name,
         email=post.email,
         password=hashed_password
    )
    return register_student(db , user)

    