from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class User(BaseModel):
    id: int
    email: EmailStr
    hashed_password: str

class ReturnUser(BaseModel):
    id: int
    email: EmailStr