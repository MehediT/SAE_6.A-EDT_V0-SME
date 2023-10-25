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
    def create_teacher(identifier, password, name, lastname, role="ROLE_TEACHER"):
        user = UserService.create_user(identifier=identifier, password=password, role=role, name=name, lastname=lastname)
        teacher = TeacherService.create_teacher_from_user(user)
        return teacher
    
    @staticmethod
    def create_teacher_from_user(user):
        teacher = Teacher(initial_name=TeacherService.get_initial(name=user.name, lastname=user.lastname), user_id=user.id)
        db.session.add(teacher)
        db.session.commit()
        return teacher

    @staticmethod
    def get_by_id(id):
        return Teacher.query.get(id)
    
    @staticmethod
    def get_by_initial(initial_name):
        return Teacher.query.filter_by(initial_name=initial_name).first()

    @staticmethod
    def delete_teacher(teacher):
        user = UserService.get_by_id(teacher.user_id)
        db.session.delete(user)
        db.session.delete(teacher)
        db.session.commit()

    @staticmethod
    def get_initial(name, lastname):
        namelist=name.split(" ")
        lastnamelist=lastname.split(" ")
        initial=""
        indexChar = 0
        for c in namelist:
            initial+=c[indexChar]
        for c in lastnamelist:
            initial+=c[indexChar] 
        
        initialExist = TeacherService.get_by_initial(initial_name=initial)

        while initialExist is not None:
            indexChar+=1
            initial = ""

            for c in namelist:
                for i in range(indexChar):
                    initial+=c[i]
            for c in lastnamelist:
                initial+=c[0]
            
            initialExist = TeacherService.get_by_initial(initial=initial)
        
        return "CG"