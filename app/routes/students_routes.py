from fastapi import APIRouter , Depends 
from app.core.dependencies import get_current_user , create_access_token , require_admin,get_db
from app.schemas.student_schema import Register , Login , ResponseRegister , LoginResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.student_service import register_user


router=APIRouter()

@router.post("/register" , response_model=ResponseRegister )
async def register_user(post:Register , db:AsyncSession=Depends(get_db), user=Depends(require_admin)):
    return register_user(post , db , user)

@router.post("/login" , response_model=LoginResponse)
async def login(post:Login , db:AsyncSession=Depends(get_db)):
    pass 