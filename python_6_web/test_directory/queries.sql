-- Отримати всі групи
SELECT * FROM groups;

-- Отримати всіх викладачів
SELECT * FROM teachers;

-- Отримати всі предмети
SELECT * FROM subjects;

-- Отримати всіх студентів та їхні оцінки
SELECT students.name, subjects.name, grades.grade
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id;