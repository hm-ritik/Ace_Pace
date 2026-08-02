from sqlalchemy import Integer , Column , String , DateTime
from app.core.database import Base
from datetime import datetime



class Student(Base):
    __tablename__="students"
    id=Column(Integer , primary_key=True, index=True)
    name=Column(String , nullable=False)
    email=Column(String , unique=True , nullable=False)
    role=Column(String , default="student")
    hashed_password=Column(String , nullable=False)
    created_at=Column(DateTime , default=datetime.utcnow)

# add below the existing Student class
class AccessRequest(Base):
    __tablename__ = "access_requests"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False)
    requested_at = Column(DateTime, default=datetime.utcnow)


 

    