from sqlalchemy.ext.asyncio import AsyncSession , create_async_engine , async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
import os 
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL=os.getenv("DATABASE_URL")


engine=create_async_engine( DATABASE_URL,
    echo=False,
    connect_args={"statement_cache_size": 0})
SessionLocal=async_sessionmaker(bind=engine , class_=AsyncSession,expire_on_commit=False)

class Base(DeclarativeBase):
    pass









  
