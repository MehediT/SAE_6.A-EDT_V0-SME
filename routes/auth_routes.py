from flask import Blueprint
from flask_jwt_extended import (create_access_token)
from flask import Flask, request, jsonify
from services.UserService import UserService
from models.User import User





auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/user', methods=['POST'])
def register():
    identifier = request.json.get('identifier')
    password = request.json.get('password')
    name = request.json.get('name')
    lastname = request.json.get('lastname')

    try:
        # Créez un nouvel utilisateur
        UserService.create_user(identifier=identifier, password=password, name=name, lastname=lastname)

        return jsonify({'message': 'Nouvel utilisateur ajouté avec succès'}),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403

@auth_bp.route('/login', methods=['POST'])
def login():

    username = request.json.get('username')
    password = request.json.get('password')

    user = UserService.get_by_identifier(username)
    if (user is not None):
        # Vérifiez le nom d'utilisateur et le mot de passe (par exemple, dans une base de données)
        # Si la vérification est réussie, générez un jeton d'accès JWT
        if (user.check_password(password)):
            additional_claims = {'role': user.role}
            access_token = create_access_token(identity=user.id, additional_claims=additional_claims)
            return {'access_token': access_token}, 200
    else:
        return {'message': 'Authentification échouée'}, 401
    
