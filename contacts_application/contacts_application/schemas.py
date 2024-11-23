from pydantic import BaseModel, EmailStr

class ContactBase(BaseModel):
    name: str
    email: EmailStr  # Використовуємо перевірку email
    phone: str

    class Config:
        orm_mode = True  # Дозволяє працювати з ORM-об'єктами

class ContactCreate(ContactBase):
    pass

class ContactResponse(ContactBase):
    id: int
    is_active: bool