from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from schemas import ContactCreate, ContactBase
from models import Contact

contacts_router = APIRouter()

# Отримати всі контакти
@contacts_router.get("/", response_model=list[ContactBase])
def read_contacts(db: Session = Depends(get_db)):
    contacts = db.query(Contact).all()
    if not contacts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contacts not found."
        )
    return contacts

# Створити контакт
@contacts_router.post("/", response_model=ContactBase, status_code=status.HTTP_201_CREATED)
def create_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    if db.query(Contact).filter(Contact.email == contact.email).first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists."
        )
    new_contact = Contact(**contact.dict())
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return new_contact

# Видалити контакт
@contacts_router.delete("/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contact not found."
        )
    db.delete(contact)
    db.commit()

@contacts_router.put("/{contact_id}", response_model=ContactBase)
def update_contact(contact_id: int, contact: ContactCreate, db: Session = Depends(get_db)):
    existing_contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if not existing_contact:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    for key, value in contact.dict().items():
        setattr(existing_contact, key, value)
    db.commit()
    db.refresh(existing_contact)
    return existing_contact