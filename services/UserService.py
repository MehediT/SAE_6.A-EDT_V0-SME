from database.config import db
from models.User import User
# import ast
# import json
# import os

class UserService:
    
    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def create_user(identifier, password, name, lastname, role):
        user = User(identifier=identifier, password=password, role=role, name=name, lastname=lastname)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def is_exist(id):
        return User.query.get(id) is not None
    
    @staticmethod
    def get_by_id(id):
        return User.query.get(id)
    
    @staticmethod
    def get_by_identifier(identifier):
        user = User.query.filter_by(identifier=identifier).first()
        return user

    @staticmethod
    def delete_user(user):
        db.session.delete(user)
        db.session.commit()

    @staticmethod
    def update_user(id, name, lastname):
        user = User.query.get(id)
        user.name = name
        user.lastname = lastname
        db.session.commit()
        return user