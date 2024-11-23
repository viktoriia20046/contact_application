from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config  # Для роботи з .env

# Отримання URL бази даних із файлу .env
SQLALCHEMY_DATABASE_URL = config("DATABASE_URL")

# Створення двигуна для роботи з базою даних
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Налаштування сесій
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовий клас для моделей
Base = declarative_base()

# Перевірка з'єднання з базою даних
try:
    with engine.connect() as connection:
        print("Database connection successful!")
except Exception as e:
    print("Database connection failed:", str(e))

# Депенд для отримання сесії бази даних
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()