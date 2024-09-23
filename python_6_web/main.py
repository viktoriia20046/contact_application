import psycopg2
from faker import Faker
import random
from datetime import datetime, timedelta

# Ініціалізація Faker для генерації випадкових даних
fake = Faker()

def create_tables():
    # Параметри підключення
    conn = psycopg2.connect(
        dbname='viktoriakubinec',
        user='viktoriakubinec',
        password='your_password',  # заміни на свій пароль
        host='localhost'
    )
    cursor = conn.cursor()

    # Створення таблиць
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS groups (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL
    );
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS teachers (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subjects (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        group_id INTEGER REFERENCES groups(id)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS grades (
        id SERIAL PRIMARY KEY,
        student_id INTEGER REFERENCES students(id),
        subject_id INTEGER REFERENCES subjects(id),
        grade INTEGER CHECK (grade >= 1 AND grade <= 12),
        date DATE NOT NULL
    );
    """)

    # Підтвердження змін
    conn.commit()

    # Закриття курсора та з'єднання
    cursor.close()
    conn.close()

def insert_fake_data():
    # Параметри підключення
    conn = psycopg2.connect(
        dbname='viktoriakubinec',
        user='viktoriakubinec',
        password='your_password',  # заміни на свій пароль
        host='localhost'
    )
    cursor = conn.cursor()

    # Додавання випадкових даних
    for _ in range(5):  # Додаємо 5 груп
        cursor.execute("INSERT INTO groups (name) VALUES (%s);", (fake.word(),))

    for _ in range(10):  # Додаємо 10 вчителів
        cursor.execute("INSERT INTO teachers (name) VALUES (%s);", (fake.name(),))

    for _ in range(15):  # Додаємо 15 предметів
        cursor.execute("INSERT INTO subjects (name) VALUES (%s);", (fake.word(),))

    for _ in range(20):  # Додаємо 20 студентів
        group_id = random.randint(1, 5)  # Випадкова група
        cursor.execute("INSERT INTO students (name, group_id) VALUES (%s, %s);", (fake.name(), group_id))

    for _ in range(30):  # Додаємо 30 оцінок
        student_id = random.randint(1, 20)  # Випадковий студент
        subject_id = random.randint(1, 15)  # Випадковий предмет
        grade = random.randint(1, 12)  # Випадкова оцінка
        date = datetime.now() - timedelta(days=random.randint(1, 365))  # Випадкова дата
        cursor.execute("INSERT INTO grades (student_id, subject_id, grade, date) VALUES (%s, %s, %s, %s);",
                       (student_id, subject_id, grade, date.date()))

    # Підтвердження змін
    conn.commit()

    # Закриття курсора та з'єднання
    cursor.close()
    conn.close()

def connect_and_show_tables():
    # Параметри підключення
    conn = psycopg2.connect(
        dbname='viktoriakubinec',
        user='viktoriakubinec',
        password='your_password',  # заміни на свій пароль
        host='localhost'
    )
    cursor = conn.cursor()

    # Виконання запиту для отримання назв таблиць
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")

    # Отримання та виведення результатів
    tables = cursor.fetchall()
    print("Список таблиць у базі даних:")
    for table in tables:
        print(table[0])  # виводить назви таблиць

    # Закриття курсора та з'єднання
    cursor.close()
    conn.close()

if __name__ == '__main__':
    create_tables()          # Створення таблиць
    insert_fake_data()       # Додавання випадкових даних
    connect_and_show_tables() # Виведення назв таблиць