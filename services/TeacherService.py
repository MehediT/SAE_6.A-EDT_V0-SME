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
        initial = "PB"
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

    # @staticmethod
    # def get_initial(name, lastname):
    #     if " " in name:
    #         namelist=name.split(" ")
    #     elif "-" in name:
    #         namelist=name.split("-")
    #     else:
    #         namelist=name.split("")
    #     if len(namelist)>=2:
    #         for c in namelist:
    #             c=c.split("")

    #     if " " in lastname:
    #         lastnamelist=lastname.split(" ")
    #     elif "-" in lastname:
    #         lastnamelist=lastname.split("-")
    #     else:
    #         lastnamelist=lastname.split("")
    #     if len(lastnamelist)>=2:
    #         for c in lastnamelist:
    #             c=c.split("")

    #     initial=""
    #     indexChar = 0

    #     initial+=name[indexChar].upper()
    #     initial+=lastname[indexChar].upper()
        
    #     initialExist = EnseignantService.get_by_initial(initial_name=initial)

    #     while initialExist is not None:

    #         indexChar+=1
    #         initial = ""

    #         for c in namelist:
    #             for i in range(indexChar):
    #                 initial+=c[i].upper()
            
    #         initialExist = EnseignantService.get_by_initial(initial=initial)

    #         if initialExist is not None:
    #             for c in lastnamelist:
    #                 for i in range(indexChar):
    #                     initial+=c[i].upper()

    #             initialExist = EnseignantService.get_by_initial(initial=initial)
        
    #     return initial