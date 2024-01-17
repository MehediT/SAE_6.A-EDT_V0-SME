from database.config import db
from models.User import User
# import ast
# import json
# import os

class UserService:
    
    @staticmethod
    def get_all_users():
        # Récupère tous les utilisateurs de la base de données.
        # :return: Liste d'objets User
        return User.query.all()
    

    @staticmethod
    def create_user(username, password, name, lastname, role):
        # Crée un nouvel utilisateur dans la base de données
        user = User(username=username, password=password, role=role, name=name, lastname=lastname)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def is_exist(id):
        # Vérifie si un utilisateur avec l'ID donné existe
        return User.query.get(id) is not None
    
    @staticmethod
    def get_by_id(id):
        # Récupère un utilisateur par son ID
        return User.query.get(id)
    
    @staticmethod
    def get_by_username(username):
        # Récupère un utilisateur par son nom d'utilisateur
        user = User.query.filter_by(username=username).first()
        return user

    @staticmethod
    def delete_user(user):
        # Supprime un utilisateur de la base de données
        db.session.delete(user)
        db.session.commit()

    @staticmethod
    def update_user(id, name, lastname):
        # Met à jour les informations de prénom et nom de famille d'un utilisateur
        user = User.query.get(id)
        user.name = name
        user.lastname = lastname
        db.session.commit()
        return user