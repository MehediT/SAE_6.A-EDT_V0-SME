from flask import Blueprint, jsonify, request
from services.WeekCommentService import WeekCommentService
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity)

week_comment_bp = Blueprint('comment', __name__)


@week_comment_bp.route('/week/comments', methods=['GET'])
@jwt_required()
def get_all_week_comments():

    try:
        # Récupérer toutes les abscences d'un étudiant
        comments = WeekCommentService.get_all_comments()   

        comments_dict = [comment.to_dict() for comment in comments]
        return jsonify(comments_dict),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    
@week_comment_bp.route('/week/comment/<id>', methods=['GET'])
@jwt_required()
def get_comment(id):
    try:
        # Récupérer toutes les abscences d'un étudiant
        comment = WeekCommentService.get_comment_by_id(id) 
        if not comment:
            return jsonify({'error': 'Salle not found'}),403  

        return jsonify(comment.to_dict()),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    

@week_comment_bp.route('/week/comment', methods=['POST'])
@jwt_required()
def create_comment():
    data = request.json

    try:
        # Créer une comment
        comment = WeekCommentService.create_comment(data)

        return jsonify(comment.to_dict()),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    
@week_comment_bp.route('/week/comment/<id>', methods=['DELETE'])
@jwt_required()
def delete_comment(id):
    try: 
        comment = WeekCommentService.delete_comment(id)

        return jsonify(comment.to_dict()),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    

@week_comment_bp.route('/week/comment/<id>', methods=['PUT'])
@jwt_required()
def update_comment(id):
    data = request.json
    if 'id' in data:
        del data['id']


    try:
        comment = WeekCommentService.update_comment(id=id, **data)

        return jsonify(comment.to_dict()),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403

    


    
    