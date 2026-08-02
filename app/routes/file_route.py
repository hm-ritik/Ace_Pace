from fastapi import APIRouter , Depends , UploaadFile , File
from app.core.dependencies import get_current_user , create_access_token , require_admin,get_db
from app.schemas.student_schema import Register , Login
from app.schemas.file_schema import UploadedFileCreate , UploadedFileResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.students_model import Student


router=APIRouter()

@router.post("/profile_picture")
async def profile_picture(profile:UploaadFile=File(...) , db:AsyncSession=Depends(get_db) , current_user:Student=Depends(get_current_user)):
    pass

@router.delete("/")
async def delete_profile_picture(db:AsyncSession=Depends(get_db) , current_user:Student=Depends(get_current_user)):
    pass


@router.post("/upload_file" ,  response_model=UploadedFileResponse)
async def upload_file(profile:UploaadFile=File(...) , db:AsyncSession=Depends(get_db) , current_user:Student=Depends(get_current_user)):
    pass

@router.get("/viewfile")
async def view_file(file_id:int , db:AsyncSession=Depends(get_db) , current_user:Student=Depends(get_current_user)):
    pass

@router.delete("/deletefile")
async def delete_file(file_id:int , db:AsyncSession=Depends(get_db) , current_user:Student=Depends(get_current_user)):
    pass



@router.get("/downloadfile")
async def download_file(file_id:int , db:AsyncSession=Depends(get_db) , current_user:Student=Depends(get_current_user)):
    pass

@router.get("/viewallfiles" , response_model=list[UploadedFileResponse])
async def view_all_files( db:AsyncSession=Depends(get_db) , current_user:Student=Depends(get_current_user)):
    pass






