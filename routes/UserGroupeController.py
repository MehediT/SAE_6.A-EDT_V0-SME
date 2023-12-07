from flask import Blueprint, jsonify, request
from services.UserGroupeService import UserGroupeService

usergroupe_bp = Blueprint('usergroupe', __name__)


@usergroupe_bp.route('/usergroupe/groupeEtudiant/<idGroupe>/<idStudent>', methods=['GET'])
def get_groupe_etudiant(idStudent,idGroupe):

    try:
        # Récupérer un étudiant via un groupe
        groupe_etudiant = UserGroupeService.get_groupe_etudiant(idStudent,idGroupe)
        if not groupe_etudiant:
            return jsonify({'error': 'Groupe not found'}),403

        return jsonify(groupe_etudiant.to_dict()),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    



@usergroupe_bp.route('/usergroupe/etudiantGroupe/<idGroupe>/<idStudent>', methods=['GET'])
def get_etudiant_by_groupe(idStudent,idGroupe):

    try:
        # Récupérer un étudiant via un groupe
        groupe_etudiant = UserGroupeService.get_etudiant_by_groupe(idStudent,idGroupe)
        if not groupe_etudiant:
            return jsonify({'error': 'Etudiant not found'}),403

        return jsonify(groupe_etudiant.to_dict()),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    

@usergroupe_bp.route('/usergroupe/delete/<idStudent>', methods=['DELETE'])
def delete_user_groupe(idStudent):

    try:
        # Récupérer un étudiant via un groupe
        groupe_etudiant = UserGroupeService.delete_user_groupe(idStudent)
        
        if not groupe_etudiant:
            return jsonify({'error': 'Etudiant not found'}),403

        return jsonify(groupe_etudiant.to_dict()),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403