from pydantic import BaseModel, ConfigDict, EmailStr

from app.models import Role


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: Role = Role.USER


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: EmailStr
    role: Role


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenPayload(BaseModel):
    sub: str
    role: Role
