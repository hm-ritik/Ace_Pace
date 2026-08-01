from sqlalchemy import Integer , Column , String , Datetime
from app.core.database import Base
from datetime import datetime



class Student(Base):
    __tablename__="students"
    id=Column(Integer , primary_key=False , index=True)
    name=Column(String , nullable=False)
    email=Column(String , unique=True , nullable=False)
    hashed_password=Column(String , nullable=False)
    created_at=Column(Datetime , default=datetime.utcnow)

 

    