from flask import Blueprint, jsonify, send_from_directory, request
from services.UserService import UserService
from services.EnseignantService import EnseignantService
from models.User import User
from functools import wraps
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity)

user_bp = Blueprint('teacher', __name__)


@user_bp.route('/teacher/create', methods=['POST'])
def create_teacher():
    identifier = request.json.get('identifier')
    password = request.json.get('password')
    name = request.json.get('name')
    lastname = request.json.get('lastname')

    try:
        # Créer un enseignant
        EnseignantService.create_teacher(identifier, password, name, lastname)

        return jsonify({'message': 'Nouveau enseignant ajouté avec succès'}),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    
@user_bp.route('/teacher/getAll', methods=['GET'])
def get_all_teacher():
    try:
        # Récupérer tous les enseignants
        EnseignantService.get_all_teachers()
        return jsonify({'message': 'Tous les enseignants sont envoyés avec succès'}),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    
@user_bp.route('/teacher/getById', methods=['GET'])
def get_by_id():
    try:
        # Récupérer un enseignant avec son ID
        EnseignantService.get_by_id()
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