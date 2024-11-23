from fastapi import FastAPI
from contacts import contacts_router

app = FastAPI()

app.include_router(contacts_router, prefix="/contacts", tags=["Contacts"])

app = FastAPI(
    title="Contacts API",
    description="REST API для управління контактами.",
    version="1.0.0",
)