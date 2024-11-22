from fastapi import FastAPI
from contacts import contacts_router

app = FastAPI()

app.include_router(contacts_router, prefix="/contacts", tags=["Contacts"])