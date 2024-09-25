import psycopg2

def create_tables():
    try:
        print("Підключення до бази...")
        conn = psycopg2.connect(
            dbname='viktoriadb',
            user='postgres',
            password='your_password',  # Заміни на свій пароль
            host='localhost'
        )
        cursor = conn.cursor()

        print("Створюємо таблиці...")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS groups (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL
        );
        """)
        print("Таблиця 'groups' створена.")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS teachers (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL
        );
        """)
        print("Таблиця 'teachers' створена.")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subjects (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            teacher_id INTEGER REFERENCES teachers(id)
        );
        """)
        print("Таблиця 'subjects' створена.")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            group_id INTEGER REFERENCES groups(id)
        );
        """)
        print("Таблиця 'students' створена.")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS grades (
            id SERIAL PRIMARY KEY,
            student_id INTEGER REFERENCES students(id),
            subject_id INTEGER REFERENCES subjects(id),
            grade INTEGER CHECK (grade >= 1 AND grade <= 12),
            date DATE NOT NULL
        );
        """)
        print("Таблиця 'grades' створена.")

        conn.commit()
        print("Таблиці створені.")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Помилка: {e}")

if __name__ == '__main__':
    create_tables()