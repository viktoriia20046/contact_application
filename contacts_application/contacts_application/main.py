from fastapi import FastAPI
from database import Base, engine
from contacts import contacts_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(contacts_router, prefix="/contacts", tags=["contacts"])