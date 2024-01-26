from xml.dom import NotFoundErr
from flask import Blueprint, jsonify, send_from_directory, request
from services.TeacherService import TeacherService
from functools import wraps
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity)
from flask import abort


# Création d'un nouveau Blueprint. C'est une façon d'organiser les routes dans Flask.
teacher_bp = Blueprint('teacher', __name__)

# Définition d'une route pour obtenir tous les enseignants. 
# Cette fonction sera appelée lorsqu'une requête GET est faite à '/teachers'.
@teacher_bp.route('/teachers', methods=['GET'])
@jwt_required()
def get_all_teacher():
    try:
        # Récupération de tous les enseignants.
        teachers = TeacherService.get_all_teachers()
        teachers_dict = [teacher.to_dict() for teacher in teachers]
        return jsonify(teachers_dict),200
    except Exception as e:
        # En cas d'erreur, retourne un message d'erreur.
        return jsonify({'error': str(e)}),403

# Définition d'une route pour obtenir un enseignant spécifique par son ID. 
# Cette fonction sera appelée lorsqu'une requête GET est faite à '/teacher/<id>'.
@teacher_bp.route('/teacher/<id>', methods=['GET'])
@jwt_required()
def get_by_idTeacher(id):
    try:
        # Récupération de l'enseignant par son ID.
        teacher = TeacherService.get_by_id(id)
        if not teacher:
            return jsonify({'error': 'Teacher not found'}),403
        return jsonify(teacher.to_dict()),200
    except Exception as e:
        # En cas d'erreur, retourne un message d'erreur.
        return jsonify({'error': str(e)}),403

# Définition d'une route pour créer un nouvel enseignant. 
# Cette fonction sera appelée lorsqu'une requête POST est faite à '/teacher'.
@teacher_bp.route('/teacher', methods=['POST'])
@jwt_required()
def create_teacher():
    # Récupération des données de la requête.
    data = request.json
    try:
        # Création de l'enseignant avec les données fournies.
        teacher = TeacherService.create_teacher(data)
        return jsonify(teacher.to_dict()), 200
    except Exception as e:
        # En cas d'erreur, retourne un message d'erreur.
        abort(500, {'error': str(e)})

# Définition d'une route pour supprimer un enseignant spécifique par son ID. 
# Cette fonction sera appelée lorsqu'une requête DELETE est faite à '/teacher/<id>'.
@teacher_bp.route('/teacher/<id>', methods=['DELETE'])
@jwt_required()
def delete_teacher(id):
    try:
        # Suppression de l'enseignant par son ID.
        teacher = TeacherService.delete_teacher(id)
        if not teacher:
            return jsonify({'error': 'Teacher not found'}),403
        return jsonify(teacher.to_dict()),200
    except Exception as e:
        # En cas d'erreur, retourne un message d'erreur.
        return jsonify({'error': str(e)}),403

# Définition d'une route pour mettre à jour un enseignant spécifique par son ID. 
# Cette fonction sera appelée lorsqu'une requête PUT est faite à '/teacher/<id>'.
@teacher_bp.route('/teacher/<id>', methods=['PUT'])
@jwt_required()
def update_teacher(id):
    # Récupération des données de la requête.
    data = request.json
    if 'id' in data:
        del data['id']
    try:
        # Mise à jour de l'enseignant avec les données fournies.
        teacher = TeacherService.update_teacher(id=id, **data)
        if not teacher:
            return jsonify({'error': 'Teacher not found'}),403
        return jsonify(teacher.to_dict()),200
    except Exception as e:
        # En cas d'erreur, retourne un message d'erreur.
        return jsonify({'error': str(e)}),403