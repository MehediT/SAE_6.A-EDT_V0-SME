from flask import Blueprint, jsonify, send_from_directory, request
from services.UserService import UserService
from models.User import User
from functools import wraps
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity)

user_bp = Blueprint('user', __name__)

@user_bp.route('/user', methods=['POST'])
def create_user():
    identifier = request.json.get('identifier')
    password = request.json.get('password')
    name = request.json.get('name')
    lastname = request.json.get('lastname')

    try:
        user = UserService.create_user(identifier, password, name, lastname)
        return jsonify(user.to_dict()),200
    except Exception as e:
        return jsonify({'error': str(e)}),403 
    

@user_bp.route('/users', methods=['GET'])
def get_all_user():
    try:
        users = UserService.get_all_users()
        users_dict = [user.to_dict() for user in users]
        return jsonify([users_dict]),200
    except Exception as e:
        return jsonify({'error': str(e)}),403
    

@user_bp.route('/user/<id>', methods=['GET'])
def get_by_idUser(id):
    try:
        user = UserService.get_by_id(id)
        if not user:
            return jsonify({'error': 'User not found'}),403  
        return jsonify(user.to_dict()),200
    except Exception as e:
        return jsonify({'error': str(e)}),403
    

@user_bp.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = UserService.get_by_id(id)
        UserService.delete_user(user)
        if not user:
            return jsonify({'error': 'User not found'}),403  
        return jsonify(user.to_dict()),200
    except Exception as e:
        return jsonify({'error': str(e)}),403
    

@user_bp.route('/user/<id>', methods=['PUT'])
def update_user(id):
    name = request.json.get('name')
    lastname = request.json.get('lastname')
    try:
        user = UserService.update_user(id, name, lastname)
        if not user:
            return jsonify({'error': 'User not found'}),403  
        return jsonify(user.to_dict()),200
    except Exception as e:
        return jsonify({'error': str(e)}),403