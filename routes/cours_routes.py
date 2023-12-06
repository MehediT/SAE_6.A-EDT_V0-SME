from flask import Blueprint, jsonify, send_from_directory, request
from services.UserService import UserService
from models.User import User
from functools import wraps
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity)
from services.CoursService import CoursService

cours_bp = Blueprint('cours', __name__)

# {
#   "date": "2023-11-28",
#   "heureDebut": "09:00",
#   "heureFin": "11:00",
#   "enseignant": "Rety",
#   "ressource": "Qualite Algorithme",
#   "promotion": "2023",
#   "groupe": "A2",
#   "salle": "B1-14"
# }
@cours_bp.route('/cours/create', methods=['POST'])
def create_cours():
    date = request.json.get('date')
    heureDebut = request.json.get('heureDebut')
    heureFin = request.json.get('heureFin')
    enseignant = request.json.get('enseignant')
    ressource = request.json.get('title')
    promotion = request.json.get('promotion')
    groupe = request.json.get('groupe')
    salle = request.json.get('salle')

    try:
        # Créez un nouveau cours
        grp = db.query.filter_by(groupe = groupe).filter_by(promotion=promotion).first().id
        CoursService.create_cours(date, heureDebut, heureFin, enseignant, ressource, promotion, grp, salle)
        return jsonify({'message': 'Nouveau cours ajouté avec succès'}),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403


@cours_bp.route('/cours/getByGroup', methods=['GET'])
def get_cours_by_groupe():
    groupe = request.json.get('groupe')

    try:
        CoursService.get_cours_by_groupe(groupe)
        return jsonify({'message': 'Cours selon le groupe envoyé avec succès'}),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    

@cours_bp.route('/cours/getByPromo', methods=['GET'])
def get_cours_by_promo():
    promo = request.json.get('promo')

    try:
        CoursService.get_cours_by_promo(promo)
        return jsonify({'message': 'Cours selon la promo envoyé avec succès'}),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403


@cours_bp.route('/cours/getTeacherSchedule', methods=['GET'])
def get_teacher_schedule():
    enseignant = request.json.get('enseignant')

    try:
        CoursService.get_teacher_schedule(enseignant)
        return jsonify({'message': 'Cours selon lenseignant envoyé avec succès'}),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    

@cours_bp.route('/cours/getAvailableSalle', methods=['GET'])
def get_salle_availability():
    salle = request.json.get('salle')

    try:
        CoursService.get_salle_availability(salle)
        return jsonify({'message': 'Salles disponibles envoyés avec succès'}),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    

@cours_bp.route('/cours/getCoursByDate', methods=['GET'])
def get_cours_by_date():
    date = request.json.get('date')

    try:
        CoursService.get_cours_by_date(date)
        return jsonify({'message': 'Cours selon les dates envoyés avec succès'}),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    

@cours_bp.route('/cours/getCoursByRessource', methods=['GET'])
def get_cours_by_ressource():
    ressource = request.json.get('ressource')

    try:
        CoursService.get_cours_by_ressource(ressource)
        return jsonify({'message': 'Cours selon la ressources envoyés avec succès'}),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    

@cours_bp.route('/cours/setGroupe', methods=['POST'])
def set_groupe():
    idCours = request.json.get('idCours')
    new_groupe = request.json.get('new_groupe')

    try:
        CoursService.set_groupe(idCours,new_groupe)
        return jsonify({'message': 'Groupe ajouté au cours avec succès'}),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    

@cours_bp.route('/cours/setPromo', methods=['POST'])
def set_promo():
    idCours = request.json.get('idCours')
    new_promo = request.json.get('new_promo')

    try:
        CoursService.set_groupe(idCours,new_promo)
        return jsonify({'message': 'Promo ajoutée au cours avec succès'}),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    

@cours_bp.route('/cours/setTeacher', methods=['POST'])
def set_teacher():
    idCours = request.json.get('idCours')
    new_enseignant = request.json.get('new_enseignant')

    try:
        CoursService.set_teacher(idCours,new_enseignant)
        return jsonify({'message': 'Enseignant ajouté au cours avec succès'}),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    

@cours_bp.route('/cours/setSalle', methods=['POST'])
def set_salle():
    idCours = request.json.get('idCours')
    new_salle = request.json.get('new_salle')

    try:
        CoursService.set_salle(idCours,new_salle)
        return jsonify({'message': 'Salle ajoutée au cours avec succès'}),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    

@cours_bp.route('/cours/setDate', methods=['POST'])
def set_date():
    idCours = request.json.get('idCours')
    new_date = request.json.get('new_date')

    try:
        CoursService.set_date(idCours,new_date)
        return jsonify({'message': 'Date ajoutée au cours avec succès'}),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    

@cours_bp.route('/cours/setRessource', methods=['POST'])
def set_ressource():
    idCours = request.json.get('idCours')
    new_ressource = request.json.get('new_ressource')

    try:
        CoursService.set_ressource(idCours,new_ressource)
        return jsonify({'message': 'Ressource ajoutée au cours avec succès'}),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    

@cours_bp.route('/cours/delete', methods=['DELETE'])
def delete_cour():
    idCours = request.json.get('idCours')

    try:
        CoursService.delete_cour(idCours)
        return jsonify({'message': 'Cours supprimé avec succès'}),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403