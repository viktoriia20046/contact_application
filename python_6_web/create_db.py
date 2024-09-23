import psycopg2

# Параметри підключення
conn = psycopg2.connect(
    dbname='viktoriakubinec',
    user='viktoriakubinec',
    password='your_password',
    host='localhost'
)

# Створення курсора
cursor = conn.cursor()

# Виконання запиту
cursor.execute("SELECT * FROM groups;")

# Отримання та виведення результатів
rows = cursor.fetchall()
for row in rows:
    print(row)

# Закриття курсора та з'єднання
cursor.close()
conn.close()