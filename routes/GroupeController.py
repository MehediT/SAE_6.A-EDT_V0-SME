from flask import Blueprint, jsonify, send_from_directory, request
from services.GroupeService import GroupeService
from models.Groupe import Groupe
from functools import wraps
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity)

groupe_bp = Blueprint('groupe', __name__)

@groupe_bp.route('/groupe', methods=['POST'])
def create_groupe():
    data = request.json
    try:
        groupe = GroupeService.create_groupe(data)
        return jsonify(groupe.to_dict()),200
    except Exception as e:
        return jsonify({'error': str(e)}),403


@groupe_bp.route('/groupes', methods=['GET'])
def get_all_groupes():
    try:
        groupes = GroupeService.get_all_groupes()
        groupes_dict = [groupe.to_dict() for groupe in groupes]
        return jsonify(groupes_dict),200
    except Exception as e:
        return jsonify({'error': str(e)}),403


@groupe_bp.route('/groupe/<id>', methods=['GET'])
def get_by_id(id):
    try:
        groupe = GroupeService.get_groupe_by_id(id)
        if not groupe:
            return jsonify({'error': 'Groupe not found'}),403
                
        return jsonify(GroupeService.get_parents(id)),200
    except Exception as e:
        return jsonify({'error': str(e)}),403
    

@groupe_bp.route('/groupe/<id>', methods=['DELETE'])
def delete_groupe(id):
    try:
        groupe = GroupeService.delete_groupe(id)
        if not groupe:
            return jsonify({'error': 'Groupe not found'}),403
        return jsonify(groupe.to_dict()),200
    except Exception as e:
        return jsonify({'error': str(e)}),403
    

@groupe_bp.route('/groupe/<id>', methods=['PUT'])
def update_groupe(id):
    data = request.json
    if 'id' in data:
        del data['id']
    try:
        groupe = GroupeService.update_groupe(id, **data)
        if not groupe:
            return jsonify({'error': 'Groupe not found'}),403
        
        return jsonify(groupe.to_dict()),200
    except Exception as e:
        return jsonify({'error': str(e)}),403
