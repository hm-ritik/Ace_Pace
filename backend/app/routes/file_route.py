from fastapi import APIRouter, Depends, UploadFile, File
from app.core.dependencies import get_current_user, get_db
from app.schemas.file_schema import UploadedFileResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.students_model import Student
from app.services import file_service

router = APIRouter()


@router.post("/profile_picture")
async def profile_picture(profile: UploadFile = File(...), db: AsyncSession = Depends(get_db), current_user: Student = Depends(get_current_user)):
    return await file_service.upload_user_profile_picture(profile, db, current_user)


@router.delete("/")
async def delete_profile_picture(db: AsyncSession = Depends(get_db), current_user: Student = Depends(get_current_user)):
    return await file_service.delete_user_profile_picture(db, current_user)


@router.post("/upload_file", response_model=UploadedFileResponse)
async def upload_file(profile: UploadFile = File(...), category: str = "general", db: AsyncSession = Depends(get_db), current_user: Student = Depends(get_current_user)):
    return await file_service.upload_user_file(profile, category, db, current_user)


@router.get("/viewfile")
async def view_file(file_id: int, db: AsyncSession = Depends(get_db), current_user: Student = Depends(get_current_user)):
    return await file_service.view_file_content(file_id, db, current_user)


@router.delete("/deletefile")
async def delete_file(file_id: int, db: AsyncSession = Depends(get_db), current_user: Student = Depends(get_current_user)):
    return await file_service.remove_file(file_id, db, current_user)


@router.get("/downloadfile")
async def download_file(file_id: int, db: AsyncSession = Depends(get_db), current_user: Student = Depends(get_current_user)):
    return await file_service.download_file_content(file_id, db, current_user)


@router.get("/viewallfiles", response_model=list[UploadedFileResponse])
async def view_all_files(db: AsyncSession = Depends(get_db), current_user: Student = Depends(get_current_user)):
    return await file_service.get_all_user_files(db, current_user)


@router.get("/profile_picture")
async def get_profile_picture(db: AsyncSession = Depends(get_db), current_user: Student = Depends(get_current_user)):
    return await file_service.view_profile_picture_content(db, current_user)




