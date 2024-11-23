from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Contact(id={self.id}, name='{self.name}', email='{self.email}', phone='{self.phone}')>"