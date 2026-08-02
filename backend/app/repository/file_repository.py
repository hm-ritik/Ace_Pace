from sqlalchemy.ext.asyncio import AsyncSession
from app.models.files_model import UploadedFiles, ProfilePicture
from sqlalchemy import select, func


async def upload_profile_picture(db: AsyncSession, post: ProfilePicture):
    db.add(post)
    await db.commit()
    await db.refresh(post)
    return post


async def delete_profile_picture(db: AsyncSession, student_id: int):
    result = await db.execute(select(ProfilePicture).where(ProfilePicture.student_id == student_id))
    picture = result.scalar_one_or_none()
    if picture is not None:
        await db.delete(picture)
        await db.commit()
        return {"Message": "Profile Picture Deleted"}
    return None


async def get_profile_picture(db: AsyncSession, student_id: int):
    result = await db.execute(select(ProfilePicture).where(ProfilePicture.student_id == student_id))
    return result.scalar_one_or_none()


async def upload_files(db: AsyncSession, post: UploadedFiles):
    db.add(post)
    await db.commit()
    await db.refresh(post)
    return post


async def delete_files(db: AsyncSession, file_id: int):
    result = await db.execute(select(UploadedFiles).where(UploadedFiles.id == file_id))
    file = result.scalar_one_or_none()
    if file is not None:
        await db.delete(file)
        await db.commit()
        return {"Message": "File Deleted"}
    return None


async def view_file(db: AsyncSession, file_id: int):
    result = await db.execute(select(UploadedFiles).where(UploadedFiles.id == file_id))
    return result.scalar_one_or_none()


async def count_files_by_category(db: AsyncSession, student_id: int, category: str):
    result = await db.execute(
        select(func.count()).where(UploadedFiles.student_id == student_id, UploadedFiles.category == category)
    )
    return result.scalar()


async def get_all_files_by_student(db: AsyncSession, student_id: int):
    result = await db.execute(select(UploadedFiles).where(UploadedFiles.student_id == student_id))
    return result.scalars().all()