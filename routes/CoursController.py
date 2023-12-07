from flask import Blueprint, jsonify, send_from_directory, request
from services.UserService import UserService
from models.User import User
from functools import wraps
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity)
from services.CoursService import CoursService

cours_bp = Blueprint('cours', __name__)



@cours_bp.route('/courses', methods=['GET'])
def get_all_courses():

    try:
        courses = CoursService.get_all_courses()   

        ressources_dict = [course.to_dict() for course in courses]
        return jsonify(ressources_dict),200
    except Exception as e:
        return jsonify({'error': str(e)}),403
    
@cours_bp.route('/course/<id>', methods=['GET'])
def get_course(id):
    try:
        course = CoursService.get_course_by_id(id) 
        if not course:
            return jsonify({'error': 'Cours not found'}),404

        return jsonify(course.to_dict()),200
    except Exception as e:
        return jsonify({'error': str(e)}),403
    

@cours_bp.route('/course', methods=['POST'])
def create_course():
    data = request.json

    try:
        resp, code = CoursService.create_course(data)
        if code >= 400:
            return jsonify(resp),code
        course = resp
        return jsonify(course.to_dict()),200
    except Exception as e:

        return jsonify({'error': str(e)}),403
    

@cours_bp.route('/course/<initial>', methods=['DELETE'])
def delete_courses(initial):
    try: 
        course = CoursService.delete_course(initial)

        return jsonify(course.to_dict()),200
    except Exception as e:

        return jsonify({'error': str(e)}),403
    

@cours_bp.route('/course/<initial>', methods=['PUT'])
def update_ressource(initial):
    data = request.json

    try:
        course = CoursService.update_course(initial, **data)

        return jsonify(course.to_dict()),200
    except Exception as e:

        return jsonify({'error': str(e)}),403
