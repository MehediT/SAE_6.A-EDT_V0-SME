from xml.dom import NotFoundErr
from flask import Blueprint, jsonify, send_from_directory, request
from services.GroupeService import GroupeService
from services.StudentService import StudentService
from functools import wraps
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity)
from flask import abort

from services.UserGroupeService import UserGroupeService

student_bp = Blueprint('student', __name__)

@student_bp.route('/students', methods=['GET'])
@jwt_required()
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
@jwt_required()
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
@jwt_required()
def create_student():
    data = request.json
    try:
        student = StudentService.create_student(data)
        return jsonify(student.to_dict()), 200

    except ValueError as ve:
        abort(400, {'error': str(ve)})

    except PermissionError as pe:
        abort(403, {'error': str(pe)})

    except NotFoundErr as nfe:
        abort(404, {'error': str(nfe)})

    except Exception as e:
        abort(500, {'error': str(e)})




@student_bp.route('/student/<id>', methods=['DELETE'])
@jwt_required()
def delete_student(id):
    try:
        student = StudentService.delete_student(id)
        if not student:
            return jsonify({'error': 'Student not found'}),403
        
        return jsonify(student.to_dict()),200
    except Exception as e:
  
        return jsonify({'error': str(e)}),403
    
@student_bp.route('/student/<id>', methods=['PUT'])
@jwt_required()
def update_student(id):
    data = request.json
    if 'id' in data:
        del data['id']
    try:
        student = StudentService.update_student(id=id, **data)
        if not student:
            return jsonify({'error': 'Student not found'}),403
        
        return jsonify(student.to_dict()),200
    except Exception as e:
  
        return jsonify({'error': str(e)}),403
    
@student_bp.route('/students/groupe/<idGroupe>', methods=['GET'])
@jwt_required()
def get_all_students_by_group(idGroupe):
    try:
        groups = GroupeService.get_tree(idGroupe)
        if not groups:
            return jsonify({'error': 'Students not found'}),403
        
        students = []
        
        for group in groups:
            students_of_group = UserGroupeService.get_etudiants_for_groupe(group)

            if students_of_group:
                students.append(students_of_group)
                
        return jsonify(students),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403