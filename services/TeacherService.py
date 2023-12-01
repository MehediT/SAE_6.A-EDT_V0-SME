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
        initial = TeacherService.get_initial(data.get("name"),data.get("lastname"))
        teacher = Teacher(initial=initial, **data)
        db.session.add(teacher)
        db.session.commit()

        return teacher
    
    @staticmethod
    def get_by_id(id):
        return Teacher.query.get(id)
    

    @staticmethod
    def delete_teacher(id):
        teacher = Teacher.query.get(id)
        db.session.delete(teacher)
        db.session.commit()
        return teacher
    

    @staticmethod
    def update_teacher(id, name: str, lastname: str, role: str, **kwargs):
        teacher = Teacher.query.get(id)
        teacher.name = name
        teacher.lastname = lastname
        teacher.role = role


        db.session.commit()
        return teacher

    @staticmethod
    def get_initial(name, lastname):
        def get_initial_from_part(part, index):
            return part[:index].upper()

        initial = get_initial_from_part(name, 1) + get_initial_from_part(lastname, 1)
        initialExist = TeacherService.get_by_initial(initial_name=initial)

        indexChar = 2

        while initialExist is not None:
            initial = ""

            for part in [name, lastname]:
                if indexChar <= len(part):
                    initial += part[:indexChar].upper()

            initialExist = TeacherService.get_by_initial(initial_name=initial)
            indexChar += 1

        return initial


    @staticmethod
    def get_by_initial(initial_name):
        teachers = TeacherService.get_all_teachers()

        for teacher in teachers:
            if teacher.initial == initial_name:
                return teacher.name
                
        return None
