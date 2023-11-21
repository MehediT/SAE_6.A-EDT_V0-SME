from flask import Blueprint, jsonify, send_from_directory, request
from services.UserService import UserService
from models.User import User
from functools import wraps
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity)



api_bp = Blueprint('api', __name__)


# Fonction de vérification du rôle
def role_required(roles):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            current_user = UserService.get_by_id(get_jwt_identity())
            if current_user.role in roles:
                return fn(*args, **kwargs)
            else:
                return jsonify(message="Accès refusé. Rôle insuffisant."), 403
        return wrapper
    return decorator
    


@api_bp.route('/test', methods=['GET'])
@jwt_required()
@role_required(roles=['ROLE_ADMIN'])
def ressource_protégée():
    current_user = get_jwt_identity()
    return {'message': 'Ceci est une ressource protégée', 'user': current_user},200
