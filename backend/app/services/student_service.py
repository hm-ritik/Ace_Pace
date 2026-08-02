from app.repository.student_repository import login_student , register_student
from app.schemas.student_schema import Register , Login 
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.students_model import Student
from fastapi import HTTPException
from app.core.security import hash_password , verify_password
from app.repository.student_repository import register_student , check_email , login_student ,update_password
from app.core.dependencies import create_access_token
from app.schemas.student_schema import ChangePassword


""" name:str = Field(min_length=2 , max_length=25)
    email: EmailStr
    hashed_password:str = Field(min_length=6 , max_length=8)

class Login(BaseModel):
    email:EmailStr
    hashed_password:str


    """


async def register_user(post:Register , db:AsyncSession , current_user:Student):
    if current_user.role != 'Admin':
        raise HTTPException(status_code=403 , detail="Not Allowed")
    existing_user=await check_email(post.email , db)
    if existing_user:
        raise HTTPException(status_code=400 , detail="User Already Exists")
    hashed_password=hash_password(post.password)
    user = Student(
    name=post.name,
    email=post.email,
    hashed_password=hashed_password
      )
    return await register_student(db, user)

async def login_user(post:Login , db:AsyncSession):
    existing= await login_student( db ,post.email )
    if existing:
        if not verify_password(
            post.password,
            existing.hashed_password
        ):
            raise HTTPException(status_code=404 , detail="User Not Found")
        token=create_access_token({"sub":post.email})
        return {"access_token": token,"token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

async def change_password(post: ChangePassword,db: AsyncSession,current_user: Student):
    if not verify_password(post.current_password,current_user.hashed_password):
        raise HTTPException(status_code=400,detail="Current password is incorrect.")

    if post.current_password == post.new_password:
        raise HTTPException(status_code=400,detail="New password must be different.")

    current_user.hashed_password = hash_password(post.new_password)
    await update_password(db, current_user)

    return {
        "message": "Password updated successfully."
    }

async def get_current_user_details(current_user: Student):
    return current_user
        


    