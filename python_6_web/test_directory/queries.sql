-- Створення таблиць

CREATE TABLE IF NOT EXISTS groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS teachers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS subjects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    teacher_id INTEGER REFERENCES teachers(id)
);

CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    group_id INTEGER REFERENCES groups(id)
);

CREATE TABLE IF NOT EXISTS grades (
    id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES students(id),
    subject_id INTEGER REFERENCES subjects(id),
    grade INTEGER CHECK (grade >= 1 AND grade <= 12),
    date DATE NOT NULL
);

SELECT s.id, s.name, AVG(g.grade) AS average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id, s.name
ORDER BY average_grade DESC
LIMIT 5;

SELECT s.id, s.name, AVG(g.grade) AS average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.subject_id = 1  -- Заміни на ID предмета
GROUP BY s.id, s.name
ORDER BY average_grade DESC
LIMIT 1;

SELECT g.id, g.name, AVG(gr.grade) AS average_grade
FROM groups g
JOIN students s ON g.id = s.group_id
JOIN grades gr ON s.id = gr.student_id
WHERE gr.subject_id = 1  -- Заміни на ID предмета
GROUP BY g.id, g.name;

SELECT AVG(grade) AS average_flow_grade
FROM grades;

SELECT sub.name
FROM subjects sub
JOIN teachers t ON sub.teacher_id = t.id
WHERE t.id = 1;  -- Заміни на ID викладача
