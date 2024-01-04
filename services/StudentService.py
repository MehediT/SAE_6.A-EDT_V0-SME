from database.config import db
from models.Student import Student
from models.relations import user_groupe
# import ast
# import json
# import os

class StudentService:
    
    @staticmethod
    def get_all_students():
        return Student.query.all()

    @staticmethod
    def create_student(data):
        student = Student(**data)
        db.session.add(student)
        db.session.commit()
        return student

    
    @staticmethod
    def get_by_id(id):
        return Student.query.filter_by(id_student=id).first()

    @staticmethod
    def delete_student(id):
        student = Student.query.filter_by(id_student=id).first()
        db.session.delete(student)
        db.session.commit()
        return student

    @staticmethod
    def update_student(id, name, lastname):
        student = Student.query.filter_by(id_student=id).first()
        student.name = name
        student.lastname = lastname
        db.session.commit()
        return student
    
    # @staticmethod
    # def get_students_by_group(idGroupe):
    #     return db.session.query(Student).join(user_groupe).filter_by(id_group=idGroupe).all()