
from pydantic import BaseModel, Field, EmailStr

class BookCreate(BaseModel):
    title: str = Field(..., min_length=1)
    author: str = Field(..., min_length=1)

class MemberCreate(BaseModel):
    name: str = Field(..., min_length=2)
    email: EmailStr

class BorrowCreate(BaseModel):
    book_id: int = Field(..., gt=0)
    member_id: int = Field(..., gt=0)
