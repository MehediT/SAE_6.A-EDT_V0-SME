from flask import Blueprint, jsonify, send_from_directory, request
from services.UserService import UserService
from services.EnseignantService import EnseignantService
from models.User import User
from functools import wraps
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity)

user_bp = Blueprint('teacher', __name__)

@user_bp.route('/user/create', methods=['POST'])
def create_user():
    identifier = request.json.get('identifier')
    password = request.json.get('password')
    name = request.json.get('name')
    lastname = request.json.get('lastname')

    try:
        # Créer un enseignant
        UserService.create_user(identifier, password, name, lastname)

        return jsonify({'message': 'Nouveau user ajouté avec succès'}),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    

@user_bp.route('/users', methods=['GET'])
def get_all_user():
    try:
        users = UserService.get_all_users()
        users_dict = [user.to_dict() for user in users]
        return jsonify([users_dict]),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    

@user_bp.route('/user/getById', methods=['GET'])
def get_by_id():
    try:
        id = request.json.get('id')
        # Récupérer un enseignant avec son ID
        UserService.get_by_id(id)
        return jsonify({'message': 'le user a bien été envoyé avec succès'}),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    

@user_bp.route('/user/delete', methods=['DELETE'])
def delete_user():
    user = request.json.get('identifier')
    try:
        # Supprimer un enseignant
        UserService.delete_user(user)
        return jsonify({'message': 'lenseignant a bien été supprimé avec succès'}),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403



@user_bp.route('/teachers', methods=['GET'])
def get_all_teacher():
    try:
        teachers = EnseignantService.get_all_teachers()
        teachers_dict = [teacher.to_dict() for teacher in teachers]
        # Récupérer tous les enseignants
        return jsonify([teachers_dict]),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    
    
@user_bp.route('/teacher/<id>', methods=['GET'])
def get_by_idTeacher(id):
    try:
        # Récupérer un enseignant avec son ID
        EnseignantService.get_by_id(id)
        return jsonify({'message': 'lenseignant a bien été envoyé avec succès'}),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    
    

@user_bp.route('/teacher/delete', methods=['DELETE'])
def delete_teacher():
    teacher = request.json.get('identifier')
    try:
        # Supprimer un enseignant
        EnseignantService.delete_teacher(teacher)
        return jsonify({'message': 'lenseignant a bien été supprimé avec succès'}),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    