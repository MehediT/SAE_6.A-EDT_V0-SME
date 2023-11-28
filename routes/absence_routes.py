from flask import Blueprint, jsonify, send_from_directory, request
from services.UserService import UserService
from models.User import User
from models.Absence import Absence
from functools import wraps
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity)
from services.CoursService import CoursService
from services.AbsenceService import AbsenceService


abscence_bp = Blueprint('absence', __name__)



@absence_bp.route('/absence/getAll', methods=['GET'])
def get_all_absence():
    
    idEtudiant = request.json.get('idEtudiant')
    
    try:
        # Récupérer toutes les abscences d'un étudiant
        AbsenceService.get_all_absences(idEtudiant)
        return jsonify({'message': 'Toutes les absences de letudiant sont envoyés avec succès'}),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    


@absence_bp.route('/absence/create', methods=['POST'])
def create_absence():
    
    idEtudiant = request.json.get('idEtudiant')
    idCours = request.json.get('idCour')
    
    try:
        # Créer une absence
        AbsenceService.create_absence(idEtudiant,idCours)
        return jsonify({'message': 'Nouvelle absence crée avec succès'}),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    


@absence_bp.route('/absence/justify', methods=['POST'])
def justify_absence():
    
    idEtudiant = request.json.get('idEtudiant')
    idCours = request.json.get('idCour')

    try:
        # Justifier l'absence d'un étudiant
        AbsenceService.justify_absence(idEtudiant,idCours)
        return jsonify({'message': 'Tous les enseignants sont envoyés avec succès'}),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403




@absence_bp.route('/absence/delete', methods=['POST'])
def delete_absence():
    
    idEtudiant = request.json.get('idEtudiant')
    idCours = request.json.get('idCour')

    try:
        # Supprimer l'absence d'un étudiant
        AbsenceService.delete_absence(idEtudiant,idCours)
        return jsonify({'message': 'Tous les enseignants sont envoyés avec succès'}),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    
