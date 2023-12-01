from flask import Blueprint, jsonify, send_from_directory, request
from services.StudentService import StudentService
from functools import wraps
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity)

student_bp = Blueprint('student', __name__)

@student_bp.route('/students', methods=['GET'])
def get_all_students():
    try:
        students = StudentService.get_all_students()
        students_dict = [student.to_dict() for student in students]
        # Récupérer tous les enseignants
        return jsonify(students_dict),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403


@student_bp.route('/student/<id>', methods=['GET'])
def get_by_student(id):
    try:
        # Récupérer un enseignant avec son ID
        student = StudentService.get_by_id(id)
        if not student:
            return jsonify({'error': 'Student not found'}),403

        return jsonify(student.to_dict()),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    

@student_bp.route('/student', methods=['POST'])
def create_teacher():
    data = request.json
    try:
        student = StudentService.create_student(data)
        return jsonify(student.to_dict()),200
    except Exception as e:
        return jsonify({'error': str(e)}),403



@student_bp.route('/student/<id>', methods=['DELETE'])
def delete_teacher(id):
    try:
        student = StudentService.delete_student(id)
        if not student:
            return jsonify({'error': 'Student not found'}),403
        
        return jsonify(student.to_dict()),200
    except Exception as e:
  
        return jsonify({'error': str(e)}),403
    
@student_bp.route('/student/<id>', methods=['PUT'])
def update_teacher(id):
    data = request.json
    try:
        student = StudentService.update_student(id, **data)
        if not student:
            return jsonify({'error': 'Student not found'}),403
        
        return jsonify(student.to_dict()),200
    except Exception as e:
  
        return jsonify({'error': str(e)}),403