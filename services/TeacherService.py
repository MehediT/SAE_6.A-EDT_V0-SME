from database.config import db
from models.Teacher import Teacher
from services.UserService import UserService

# import ast
# import json
# import os

class TeacherService:
    
    @staticmethod
    def get_all_teachers():
        return Teacher.query.all()

    @staticmethod
    def create_teacher(data):
        teacher = Teacher(**data)
        db.session.add(teacher)
        db.session.commit()

        return teacher
    
    @staticmethod
    def get_by_id(id):
        return Teacher.query.filter_by(id_teacher=id).first()
    

    @staticmethod
    def delete_teacher(id):
        teacher = Teacher.query.filter_by(id_teacher=id).first()
        db.session.delete(teacher)
        db.session.commit()
        return teacher
    

    @staticmethod
    def update_teacher(id, name: str, lastname: str,activated: bool, **kwargs):
        teacher = Teacher.query.filter_by(id_teacher=id).first()
        teacher.name = name
        teacher.lastname = lastname
        teacher.activated = activated
        # teacher.role = role


        db.session.commit()
        return teacher


