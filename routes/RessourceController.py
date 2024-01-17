from xml.dom import NotFoundErr
from flask import Blueprint, jsonify, request
from services.RessourcesService import RessourcesService
from flask import abort
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity)

ressource_bp = Blueprint('ressource', __name__)

@ressource_bp.route('/ressources', methods=['GET'])
@jwt_required()
def get_all_ressources():

    try:
        ressources = RessourcesService.get_all_ressources()   

        ressources_dict = [ressource.to_dict() for ressource in ressources]
        return jsonify(ressources_dict),200
    except Exception as e:
        return jsonify({'error': str(e)}),403
    
@ressource_bp.route('/ressource/<initial>', methods=['GET'])
@jwt_required()
def get_ressource(initial):
    try:
        ressource = RessourcesService.get_resource_by_initial(initial) 
        if not ressource:
            return jsonify({'error': 'Ressource not found'}),403  

        return jsonify(ressource.to_dict()),200
    except Exception as e:
        return jsonify({'error': str(e)}),403

@ressource_bp.route('/ressource', methods=['POST'])
@jwt_required()
def create_ressource():
    data = request.json

    try:
        ressource = RessourcesService.create_resource(data)
        return jsonify(ressource.to_dict()), 200

    except ValueError as ve:
        abort(400, {'error': str(ve)})

    except PermissionError as pe:
        abort(403, {'error': str(pe)})

    except NotFoundErr as nfe:
        abort(404, {'error': str(nfe)})

    except Exception as e:
        abort(500, {'error': str(e)})

    
@ressource_bp.route('/ressource/<initial>', methods=['DELETE'])
@jwt_required()
def delete_ressource(initial):
    try: 
        ressource = RessourcesService.delete_ressource(initial)

        return jsonify(ressource.to_dict()),200
    except Exception as e:

        return jsonify({'error': str(e)}),403
    

@ressource_bp.route('/ressource/<initial>', methods=['PUT'])
@jwt_required()
def update_ressource(initial):

    data = request.json
    if 'initial' in data:
        del data['initial']

    try:
        ressource = RessourcesService.update_ressource(initial=initial,**data)

        return jsonify(ressource.to_dict()),200
    except Exception as e:

        return jsonify({'error': str(e)}),403
    
    

# @ressource_bp.route('/salle/<name>', methods=['PUT'])
# def update_room(name):
#     ordi = request.json.get('ordi')
#     tableauNumerique = request.json.get('tableauNumerique')
#     videoProj = request.json.get('videoProjecteur')

#     try:
#         salle = SalleService.update_salle(name, ordi, tableauNumerique, videoProj)

#         return jsonify(salle.to_dict()),200
#     except Exception as e:
#         # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
#         # db.session.rollback()
#         return jsonify({'error': str(e)}),403