from flask import Blueprint, jsonify, send_from_directory, request
from services.EnseignantService import EnseignantService
from functools import wraps
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity)

teacher_bp = Blueprint('teacher', __name__)

@teacher_bp.route('/teachers', methods=['GET'])
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
    
    
@teacher_bp.route('/teacher/<id>', methods=['GET'])
def get_by_idTeacher(id):
    try:
        # Récupérer un enseignant avec son ID
        teacher = EnseignantService.get_by_id(id)
        teacher_dict = [teacher_dict]
        return jsonify([teacher_dict]),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    
    

@teacher_bp.route('/teacher/delete', methods=['DELETE'])
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