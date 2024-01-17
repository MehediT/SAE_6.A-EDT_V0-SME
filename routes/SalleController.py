from xml.dom import NotFoundErr
from flask import Blueprint, jsonify, request
from services.SalleService import SalleService
from flask import abort
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity)

salle_bp = Blueprint('salle', __name__)


@salle_bp.route('/salles', methods=['GET'])
@jwt_required()
def get_all_rooms():

    try:
        # Récupérer toutes les abscences d'un étudiant
        salles = SalleService.get_all_salles()   

        salles_dict = [salle.to_dict() for salle in salles]
        return jsonify(salles_dict),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    
@salle_bp.route('/salle/<name>', methods=['GET'])
@jwt_required()
def get_room(name):
    try:
        # Récupérer toutes les abscences d'un étudiant
        salle = SalleService.get_salle_by_name(name) 
        if not salle:
            return jsonify({'error': 'Salle not found'}),403  

        return jsonify(salle.to_dict()),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403

@salle_bp.route('/salle', methods=['POST'])
@jwt_required()
def create_room():
    data = request.json

    try:
        salle = SalleService.create_salle(data)
        return jsonify(salle.to_dict()), 200

    except ValueError as ve:
        abort(400, {'error': str(ve)})

    except PermissionError as pe:
        abort(403, {'error': str(pe)})

    except NotFoundErr as nfe:
        abort(404, {'error': str(nfe)})

    except Exception as e:
        abort(500, {'error': str(e)})

    
@salle_bp.route('/salle/<name>', methods=['DELETE'])
@jwt_required()
def delete_room(name):
    try: 
        salle = SalleService.delete_salle(name)

        return jsonify(salle.to_dict()),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    

@salle_bp.route('/salle/<name>', methods=['PUT'])
@jwt_required()
def update_room(name):
    data = request.json
    if 'name' in data:
        del data['name']


    try:
        salle = SalleService.update_salle(name=name, **data)

        return jsonify(salle.to_dict()),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403

    


    
    