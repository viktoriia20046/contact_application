import psycopg2
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

def insert_fake_data():
    print("Запускаємо вставку даних...")  # Додаємо виведення для перевірки
    # Параметри підключення
    conn = psycopg2.connect(
        dbname='viktoriakubinec',
        user='viktoriakubinec',
        password='your_password',  # Заміни на свій пароль
        host='localhost'
    )
    print("Підключено до бази даних")  # Додаємо виведення для перевірки
    cursor = conn.cursor()

    # Створення груп
    for _ in range(3):  # 3 групи
        cursor.execute("INSERT INTO groups (name) VALUES (%s);", (fake.word(),))
        print("Група додана")  # Додаємо виведення для перевірки

    # Створення викладачів
    for _ in range(5):  # 5 викладачів
        cursor.execute("INSERT INTO teachers (name) VALUES (%s);", (fake.name(),))
        print("Викладач доданий")  # Додаємо виведення для перевірки

    # Створення предметів
    for _ in range(8):  # 8 предметів
        teacher_id = random.randint(1, 5)  # Викладач для кожного предмета
        cursor.execute("INSERT INTO subjects (name, teacher_id) VALUES (%s, %s);", (fake.word(), teacher_id))
        print("Предмет доданий")  # Додаємо виведення для перевірки

    # Створення студентів
    for _ in range(30):  # 30 студентів
        group_id = random.randint(1, 3)  # Випадкова група
        cursor.execute("INSERT INTO students (name, group_id) VALUES (%s, %s);", (fake.name(), group_id))
        print("Студент доданий")  # Додаємо виведення для перевірки

    # Створення оцінок для студентів
    for _ in range(500):  # Додаємо 500 оцінок
        student_id = random.randint(1, 30)  # Випадковий студент
        subject_id = random.randint(1, 8)  # Випадковий предмет
        grade = random.randint(1, 12)  # Випадкова оцінка
        date = datetime.now() - timedelta(days=random.randint(1, 365))  # Випадкова дата
        cursor.execute("INSERT INTO grades (student_id, subject_id, grade, date) VALUES (%s, %s, %s, %s);",
                       (student_id, subject_id, grade, date.date()))
        print("Оцінка додана")  # Додаємо виведення для перевірки

    # Підтвердження змін
    conn.commit()
    cursor.close()
    conn.close()
    print("Дані успішно додані")  # Додаємо виведення для перевірки

if __name__ == '__main__':
    print("Запускаємо скрипт")  # Додаємо виведення для перевірки
    insert_fake_data()
    