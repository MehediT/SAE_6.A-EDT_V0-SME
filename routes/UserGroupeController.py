from flask import Blueprint, jsonify, request
from services.UserGroupeService import UserGroupeService

usergroupe_bp = Blueprint('usergroupe', __name__)



@usergroupe_bp.route('/usergroupe/addGroupeEtudiant', methods=['POST'])
def add_user_to_group():

    idStudent = request.json["idStudent"]
    idGroupe = request.json["idGroupe"]
    
    try:
        # Ajouter un étudiant à un groupe
        groupe_etudiant = UserGroupeService.add_user_to_group(idStudent,idGroupe)


        return jsonify(groupe_etudiant.to_dict()),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403




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
    
@usergroupe_bp.route('/usergroupe/groupe/<idGroupe>', methods=['GET'])
def get_etudiants_for_groupe(idGroupe):
    try:
        # Récupérer tous les etudiants d'un groupe
        etudiants = UserGroupeService.get_etudiants_for_groupe(idGroupe)
        if not etudiants:
            return jsonify({'error': 'Etudiants not found'}),201

        return jsonify(etudiants),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    
@usergroupe_bp.route('/usergroupe/groupForStudent/<idEtudiant>', methods=['GET'])
def get_groupes_for_student(idEtudiant):
    try:
        # Récupérer tous les groupes d'un etudiant
        groupes = UserGroupeService.get_groupes_for_student(idEtudiant)
        if not groupes:
            return jsonify({'error': 'Groupe not found'}),201

        return jsonify(groupes),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403