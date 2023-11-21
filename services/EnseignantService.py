from database.config import db
from models.Enseignant import Enseignant
from services.UserService import UserService

# import ast
# import json
# import os

class EnseignantService:
    
    @staticmethod
    def get_all_teachers():
        return Enseignant.query.all()

    @staticmethod
    def create_teacher(identifier, password, name, lastname, role="ROLE_TEACHER"):
        user = UserService.create_user(identifier=identifier, password=password, role=role, name=name, lastname=lastname)
        teacher = EnseignantService.create_teacher_from_user(user)
        return teacher
    
    @staticmethod
    def create_teacher_from_user(user):
        teacher = Enseignant(initial_name=EnseignantService.get_initial(name=user.name, lastname=user.lastname), user_id=user.id)
        db.session.add(teacher)
        db.session.commit()
        return teacher

    @staticmethod
    def get_by_id(id):
        return Enseignant.query.get(id)
    
    @staticmethod
    def get_by_initial(initial_name):
        return Enseignant.query.filter_by(initial_name=initial_name).first()

    @staticmethod
    def delete_teacher(teacher):
        user = UserService.get_by_id(teacher.user_id)
        db.session.delete(user)
        db.session.delete(teacher)
        db.session.commit()

    @staticmethod
    def get_initial(name, lastname):
        if " " in name:
            namelist=name.split(" ")
        elif "-" in name:
            namelist=name.split("-")
        else:
            namelist=name.split("")
        if len(namelist)>=2:
            for c in namelist:
                c=c.split("")

        if " " in lastname:
            lastnamelist=lastname.split(" ")
        elif "-" in lastname:
            lastnamelist=lastname.split("-")
        else:
            lastnamelist=lastname.split("")
        if len(lastnamelist)>=2:
            for c in lastnamelist:
                c=c.split("")

        initial=""
        indexChar = 0

        initial+=name[indexChar].upper()
        initial+=lastname[indexChar].upper()
        
        initialExist = EnseignantService.get_by_initial(initial_name=initial)

        while initialExist is not None:

            indexChar+=1
            initial = ""

            for c in namelist:
                for i in range(indexChar):
                    initial+=c[i].upper()
            
            initialExist = EnseignantService.get_by_initial(initial=initial)

            if initialExist is not None:
                for c in lastnamelist:
                    for i in range(indexChar):
                        initial+=c[i].upper()

                initialExist = EnseignantService.get_by_initial(initial=initial)
        
        return "CG"