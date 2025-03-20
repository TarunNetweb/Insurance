from pydantic import BaseModel, EmailStr

class UserRegisterRequest(BaseModel):
    username: str
    email: EmailStr
    password: str
    role:str

class UserLoginRequest(BaseModel):
    username: str
    password: str
