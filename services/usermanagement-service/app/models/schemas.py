from pydantic import BaseModel, EmailStr


class UpdateUserRequest(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    password: str
    role: str  