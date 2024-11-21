from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import ContactCreate, Contact
from models import Contact
from typing import List

contacts_router = APIRouter()

@contacts_router.get("/", response_model=List[Contact])
def read_contacts(db: Session = Depends(get_db)):
    return db.query(Contact).all()

@contacts_router.post("/", response_model=Contact)
def create_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    db_contact = Contact(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact