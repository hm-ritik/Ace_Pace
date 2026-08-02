from pydantic import BaseModel,  EmailStr, Field, field_validator ,  ConfigDict

from datetime import datetime



class Register(BaseModel):
    name:str = Field(min_length=2 , max_length=25)
    email: EmailStr
    password:str = Field(min_length=6 , max_length=8)

class ResponseRegister(BaseModel):
    id:int
    name:str
    email:EmailStr
    created_at:datetime

class ChangePassword(BaseModel):
    current_password: str = Field(min_length=6, max_length=8)
    new_password: str = Field(min_length=6, max_length=8)    




class Login(BaseModel):
    email:EmailStr
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str

    model_config = {
            "from_attributes": True
        }

class CurrentUser(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str

    model_config = {
        "from_attributes": True
    }    

        





    



 