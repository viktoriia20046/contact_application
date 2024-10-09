import argparse
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from faker import Faker
import random

Base = declarative_base()

# Моделі
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    fullname = Column(String, nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship('Group', back_populates='students')


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    students = relationship('Student', back_populates='group')


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    fullname = Column(String, nullable=False)
    subjects = relationship('Subject', cascade="all, delete", back_populates='teacher')


class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    teacher = relationship('Teacher', back_populates='subjects')
    grades = relationship('Grade', cascade="all, delete", back_populates='subject')


class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    grade = Column(Float, nullable=False)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    date_received = Column(Date)
    student = relationship('Student')
    subject = relationship('Subject', back_populates='grades')


# Налаштування бази даних
engine = create_engine('postgresql://viktoriakubinec:@localhost:5432/mydatabase')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Заповнення бази даних випадковими даними
def seed_data():
    fake = Faker()
    groups = ['Group A', 'Group B', 'Group C']
    group_objects = [Group(name=group) for group in groups]
    session.add_all(group_objects)
    session.commit()
    
    teachers = [Teacher(fullname=fake.name()) for _ in range(3)]
    session.add_all(teachers)
    session.commit()
    
    subjects = ['Math', 'Science', 'History']
    subject_objects = [Subject(name=subject, teacher=random.choice(teachers)) for subject in subjects]
    session.add_all(subject_objects)
    session.commit()

    for _ in range(30):
        student = Student(fullname=fake.name(), group=random.choice(group_objects))
        session.add(student)
        session.commit()

        for subject in subject_objects:
            grade = Grade(grade=random.uniform(60, 100), student=student, subject=subject, date_received=fake.date_this_year())
            session.add(grade)
        session.commit()
    
    print("База даних успішно заповнена випадковими даними.")

# CRUD функції
def create_teacher(name):
    teacher = Teacher(fullname=name)
    session.add(teacher)
    session.commit()
    print(f'Вчитель {name} створений.')

def list_teachers():
    teachers = session.query(Teacher).all()
    for teacher in teachers:
        print(teacher.fullname)

def update_teacher(teacher_id, name):
    teacher = session.query(Teacher).filter(Teacher.id == teacher_id).first()
    if teacher:
        teacher.fullname = name
        session.commit()
        print(f'Вчитель {teacher_id} оновлений.')
    else:
        print(f'Вчитель з id {teacher_id} не знайдений.')

# Функція для видалення вчителя разом із предметами та оцінками
def remove_teacher_with_subjects(teacher_id):
    teacher = session.query(Teacher).filter(Teacher.id == teacher_id).first()
    
    if not teacher:
        print(f"Вчитель з id {teacher_id} не знайдений.")
        return

    # Видаляємо всі предмети та пов'язані з ними оцінки завдяки каскадному видаленню
    session.delete(teacher)
    session.commit()
    
    print(f"Вчитель {teacher_id} та всі його предмети і оцінки були успішно видалені.")

# CLI інтерфейс для роботи з вчителями
def main():
    parser = argparse.ArgumentParser(description="CRUD операції для вчителів")
    parser.add_argument("--action", "-a", choices=["create", "list", "update", "remove"], required=True, help="Дія: create, list, update, remove")
    parser.add_argument("--model", "-m", required=True, choices=["Teacher"], help="Модель: Teacher")
    parser.add_argument("--name", "-n", help="Ім'я вчителя")
    parser.add_argument("--id", help="ID вчителя", type=int)

    args = parser.parse_args()

    if args.model == "Teacher":
        if args.action == "create" and args.name:
            create_teacher(args.name)
        elif args.action == "list":
            list_teachers()
        elif args.action == "update" and args.id and args.name:
            update_teacher(args.id, args.name)
        elif args.action == "remove" and args.id:
            remove_teacher_with_subjects(args.id)
        else:
            print("Неправильні аргументи для дії.")

if __name__ == '__main__':
    seed_data()  # За бажанням, можеш закоментувати цей рядок, якщо не потрібно кожного разу заповнювати базу даних
    main()