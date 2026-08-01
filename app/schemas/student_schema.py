from pydantic import BaseModel,  EmailStr, Field, field_validator ,  ConfigDict

from datetime import datetime



class Register(BaseModel):
    name:str = Field(min_length=2 , max_length=25)
    email: EmailStr
    hashed_password:str = Field(min_length=6 , max_length=8)

class ResponseRegister(BaseModel):
    id:int
    name:str
    email:EmailStr
    created_at:datetime




class Login(BaseModel):
    email:EmailStr
    hashed_password:str

class LoginResponse(BaseModel):
    id:int
    name:str
    email:EmailStr
    created_at:datetime


    model_config = {
            "from_attributes": True
        }

        





    



 