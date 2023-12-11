from flask import Blueprint, jsonify, send_from_directory, request
from services.TeacherService import TeacherService
from functools import wraps
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity)

teacher_bp = Blueprint('teacher', __name__)

@teacher_bp.route('/teachers', methods=['GET'])
@jwt_required()
def get_all_teacher():
    try:
        teachers = TeacherService.get_all_teachers()
        teachers_dict = [teacher.to_dict() for teacher in teachers]
        # Récupérer tous les enseignants
        return jsonify(teachers_dict),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403


@teacher_bp.route('/teacher/<id>', methods=['GET'])
def get_by_idTeacher(id):
    try:
        # Récupérer un enseignant avec son ID
        teacher = TeacherService.get_by_id(id)
        if not teacher:
            return jsonify({'error': 'Teacher not found'}),403

        return jsonify(teacher.to_dict()),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    

@teacher_bp.route('/teacher', methods=['POST'])
def create_teacher():
    data = request.json
    try:
        teacher = TeacherService.create_teacher(data)
        return jsonify(teacher.to_dict()),200
    except Exception as e:
        return jsonify({'error': str(e)}),403



@teacher_bp.route('/teacher/<id>', methods=['DELETE'])
def delete_teacher(id):
    try:
        teacher = TeacherService.delete_teacher(id)
        if not teacher:
            return jsonify({'error': 'Teacher not found'}),403
        
        return jsonify(teacher.to_dict()),200
    except Exception as e:
  
        return jsonify({'error': str(e)}),403
    
@teacher_bp.route('/teacher/<id>', methods=['PUT'])
def update_teacher(id):
    data = request.json
    if 'id' in data:
        del data['id']
    try:
        teacher = TeacherService.update_teacher(id=id, **data)
        if not teacher:
            return jsonify({'error': 'Teacher not found'}),403
        
        return jsonify(teacher.to_dict()),200
    except Exception as e:
  
        return jsonify({'error': str(e)}),403