from sqlalchemy import func, desc
from main import session, Student, Grade, Group, Subject, Teacher

# 1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів
def select_1():
    return session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .join(Grade)\
        .group_by(Student.id)\
        .order_by(desc('avg_grade'))\
        .limit(5)\
        .all()

# 2. Знайти студента із найвищим середнім балом з певного предмета
def select_2(subject_name):
    return session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .join(Grade)\
        .join(Subject)\
        .filter(Subject.name == subject_name)\
        .group_by(Student.id)\
        .order_by(desc('avg_grade'))\
        .first()

# 3. Знайти середній бал у групах з певного предмета
def select_3(subject_name):
    return session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .join(Student)\
        .join(Grade)\
        .join(Subject)\
        .filter(Subject.name == subject_name)\
        .group_by(Group.id)\
        .all()

# 4. Знайти середній бал на потоці (по всій таблиці оцінок)
def select_4():
    return session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')).first()

# 5. Знайти які курси читає певний викладач
def select_5(teacher_name):
    return session.query(Subject.name)\
        .join(Teacher)\
        .filter(Teacher.fullname == teacher_name)\
        .all()

# 6. Знайти список студентів у певній групі
def select_6(group_name):
    return session.query(Student.fullname)\
        .join(Group)\
        .filter(Group.name == group_name)\
        .all()

# 7. Знайти оцінки студентів у окремій групі з певного предмета
def select_7(group_name, subject_name):
    return session.query(Student.fullname, Grade.grade)\
        .join(Group)\
        .join(Grade)\
        .join(Subject)\
        .filter(Group.name == group_name, Subject.name == subject_name)\
        .all()

# 8. Знайти середній бал, який ставить певний викладач зі своїх предметів
def select_8(teacher_name):
    return session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .join(Subject)\
        .join(Teacher)\
        .filter(Teacher.fullname == teacher_name)\
        .all()

# 9. Знайти список курсів, які відвідує певний студент
def select_9(student_name):
    return session.query(Subject.name)\
        .join(Grade)\
        .join(Student)\
        .filter(Student.fullname == student_name)\
        .all()

# 10. Список курсів, які певному студенту читає певний викладач
def select_10(student_name, teacher_name):
    return session.query(Subject.name)\
        .join(Grade)\
        .join(Student)\
        .join(Teacher)\
        .filter(Student.fullname == student_name, Teacher.fullname == teacher_name)\
        .all()