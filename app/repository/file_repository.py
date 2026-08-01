from sqlalchemy.ext.asyncio import AsyncSession 
from app.models.files_model import UploadedFiles 
from sqlalchemy import select , func
from app.schemas.file_schema import UploadedFileCreate


async def upload_profile_picture(db:AsyncSession ,post:UploadedFileCreate):
    db.add(post)
    await db.commit()
    await db.refresh(post)
    return post

async def delete_profile_picture(db:AsyncSession , student_id:int):
    post=await db.execute(select(UploadedFiles).where(UploadedFiles.student_id==student_id))
    result= post.scalar_one_or_none()
    if result is not None:
        db.delete(result)
        return{"Message": "Profile Picture Deleted"}
    return None

async def upload_files(db:AsyncSession , post:UploadedFileCreate):
    db.add(post)
    await db.commit()
    await db.refresh(post)
    return post

async def delete_files(db:AsyncSession , file_id=int):
     post=await db.execute(select(UploadedFiles).where(UploadedFiles.id==file_id))
     result= post.scalar_one_or_none()
     if result is not None:
            await db.delete(result)
            await db.commit()
            return{"Message": "File Deleted"}
     return None

async def view_file(db:AsyncSession , file_id:int):
     post=await db.execute(select(UploadedFiles).where(UploadedFiles.id==file_id))
     result=post.scalar_one_or_none()
     return result

async def count_files_by_category(db: AsyncSession,student_id: int,category: str):
    result = await db.execute(
        select(func.count()).where(UploadedFiles.student_id == student_id,UploadedFiles.category == category))
    return result.scalar()

async def get_all_files_by_student(db: AsyncSession, student_id: int):
    result = await db.execute(
        select(UploadedFiles).where(UploadedFiles.student_id == student_id))
    return result.scalars().all()
    


     



