from typing import List, Optional
from pydantic import BaseModel

class ContactBase(BaseModel):
    name: str
    phone: str
    email: str

class ContactCreate(ContactBase):
    pass

class Contact(ContactBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    contacts: List[Contact] = []

    class Config:
        orm_mode = True