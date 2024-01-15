from flask import Blueprint, jsonify, send_from_directory, request
from services.UserService import UserService
from models.User import User
from functools import wraps
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity)
from services.CoursService import CoursService

cours_bp = Blueprint('cours', __name__)



@cours_bp.route('/courses', methods=['GET'])
@jwt_required()
def get_all_courses():

    try:
        current_user = get_jwt_identity()
        user : User = UserService.get_by_id(current_user)
        courses = CoursService.get_all_courses(request.args, user=user )   

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
        
        warning_with_result = resp
        if code > 200:
            return jsonify(warning_with_result),code
        
        course = resp
        return jsonify(course.to_dict()),code
    except Exception as e:

        return jsonify({'error': str(e)}),403
    

@cours_bp.route('/course/<id>', methods=['DELETE'])
def delete_course(id):
    try: 
        course = CoursService.delete_course(id)

        return jsonify(course.to_dict()),200
    except Exception as e:

        return jsonify({'error': str(e)}),403
    

@cours_bp.route('/course/<id>', methods=['PUT'])
def update_course(id):
    data = request.json
    if 'id' in data:
        del data['id']
    try:
        resp, code = CoursService.update_course(id, **data)

        if code >= 400:
            return jsonify(resp),code
        
        warning_with_result = resp
        if code > 200:
            return jsonify(warning_with_result),code
        
        course = resp
        return jsonify(course.to_dict()),code

        return jsonify(course.to_dict()),200
    except Exception as e:

        return jsonify({'error': str(e)}),403
    

@cours_bp.route('/courses/publish', methods=['PUT'])
def publish_all():

    try:
        courses = CoursService.publish()
        courses_dict = [course.to_dict() for course in courses]
        return jsonify(courses_dict),200
    except Exception as e:

        return jsonify({'error': str(e)}),403

@cours_bp.route('/courses/cancel', methods=['DELETE'])
def cancel_all():

    try:
        courses = CoursService.cancel()
        courses_dict = [course.to_dict() for course in courses]
        return jsonify(courses_dict),200
    except Exception as e:

        return jsonify({'error': str(e)}),403   


@cours_bp.route('/courses/paste', methods=['POST']) 
def paste_all():
    data = request.json

    try:
        courses = CoursService.paste(**data)
        courses_dict = [course.to_dict() for course in courses]
        return jsonify(courses_dict),200
    except Exception as e:

        return jsonify({'error': str(e)}),403
    
@cours_bp.route('/courses/duplicate', methods=['POST']) 
def duplicate_all():
    data = request.json

    try:
        courses = CoursService.duplicate(**data)
        courses_dict = [course.to_dict() for course in courses]
        return jsonify(courses_dict),200
    except Exception as e:

        return jsonify({'error': str(e)}),403
    
@cours_bp.route('/courses/stats/<id_teacher>', methods=['GET'])
def get_stats_teacher(id_teacher):
    try:
        courses = CoursService.get_courses_by_teacher(id_teacher)
        
        name_courses = {course.initial_ressource for course in courses}
        stats = []
        total_minutes = 0
                
        for nc in name_courses:
            duration_nc_minutes = 0
            
            for course in courses:
                if nc == course.initial_ressource:
                    duration = course.end_time - course.start_time
                    minutes = duration.total_seconds() / 60
                    
                    duration_nc_minutes += minutes
                    total_minutes += minutes
                    
            hours, minutes = divmod(duration_nc_minutes, 60)
            stats.append({'name': nc, 'hours': hours, 'minutes': minutes})
        
        total_hours, total_minutes = divmod(total_minutes, 60)
        stats.append({'name': 'total', 'hours': total_hours, 'minutes': total_minutes})
        print("stats", stats)             
            
        return jsonify(stats),200
    except Exception as e:
        return jsonify({'error': str(e)}),403
