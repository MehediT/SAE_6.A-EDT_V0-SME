from database.config import db
from models.Student import Student
# import ast
# import json
# import os

class StudentService:
    
    @staticmethod
    def get_all_students():
        return Student.query.all()

    @staticmethod
    def create_student(data):
        student = Student(data)
        db.session.add(student)
        db.session.commit()
        return student

    
    @staticmethod
    def get_by_id(id):
        return Student.query.get(id)

    @staticmethod
    def delete_student(id):
        student = Student.query.get(id)
        db.session.delete(student)
        db.session.commit()
        return student

    @staticmethod
    def update_student(id, name, lastname):
        student = Student.query.get(id)
        student.name = name
        student.lastname = lastname
        db.session.commit()
        return student