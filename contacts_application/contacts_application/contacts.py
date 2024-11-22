from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import ContactCreate
from models import Contact

contacts_router = APIRouter()

@contacts_router.get("/")
def read_contacts(db: Session = Depends(get_db)):
    return db.query(Contact).all()

@contacts_router.post("/")
def create_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    new_contact = Contact(**contact.dict())
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return new_contact