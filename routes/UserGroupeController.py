from flask import Blueprint, jsonify, request
from services.UserGroupeService import UserGroupeService

usergroupe_bp = Blueprint('usergroupe', __name__)



@usergroupe_bp.route('/usergroupe/addGroupeEtudiant', methods=['POST'])
def add_user_to_group():
    idStudent = request.json["idStudent"]
    idGroupe = request.json["idGroupe"]
    
    try:
        UserGroupeService.add_user_to_group(idStudent, idGroupe)
        return jsonify({"message": "Utilisateur ajouté au groupe avec succès"}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 403


@usergroupe_bp.route('/usergroupe/groupeEtudiant/<idGroupe>/<idStudent>', methods=['GET'])
def get_groupe_etudiant(idStudent,idGroupe):

    try:
        groupe_etudiant = UserGroupeService.get_groupe_etudiant(idStudent,idGroupe)
        if not groupe_etudiant:
            return jsonify({'error': 'Groupe not found'}),403

        return jsonify(groupe_etudiant.to_dict()),200
    except Exception as e:
        return jsonify({'error': str(e)}),403
    
@usergroupe_bp.route('/usergroupe/etudiantGroupe/<idGroupe>/<idStudent>', methods=['GET'])
def get_etudiant_by_groupe(idStudent,idGroupe):

    try:
        groupe_etudiant = UserGroupeService.get_etudiant_by_groupe(idStudent,idGroupe)
        if not groupe_etudiant:
            return jsonify({'error': 'Etudiant not found'}),403

        return jsonify(groupe_etudiant.to_dict()),200
    except Exception as e:
        return jsonify({'error': str(e)}),403
    

@usergroupe_bp.route('/usergroupe/delete/<idStudent>', methods=['DELETE'])
def delete_user_groupe(idStudent):
    try:
        UserGroupeService.delete_user_groupe(idStudent)
        return jsonify({"message": "Utilisateur supprimé du groupe avec succès"}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 403
    
@usergroupe_bp.route('/usergroupe/groupe/<idGroupe>', methods=['GET'])
def get_etudiants_for_groupe(idGroupe):
    try:
        etudiants = UserGroupeService.get_etudiants_for_groupe(idGroupe)
        if not etudiants:
            return jsonify({'error': 'Etudiants not found'}),201

        return jsonify(etudiants),200
    except Exception as e:
        return jsonify({'error': str(e)}),403
    
@usergroupe_bp.route('/usergroupe/groupForStudent/<idEtudiant>', methods=['GET'])
def get_groupes_for_student(idEtudiant):
    try:
        groupes = UserGroupeService.get_groupes_for_student(idEtudiant)
        if not groupes:
            return jsonify({'error': 'Groupe not found'}),201

        return jsonify(groupes),200
    except Exception as e:
        return jsonify({'error': str(e)}),403
    
@usergroupe_bp.route('/usergroupe/modify/<idStudent>/<newIdGroupe>/<idGroupe>', methods=['PUT'])
def update_student_group(idStudent, newIdGroupe, idGroupe):
    try:
        result = UserGroupeService.update_student_group(idStudent, newIdGroupe, idGroupe)

        if "error" in result:
            return jsonify({'error': result["error"]}), 403

        return jsonify({'message': result["message"]}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 403
    
@usergroupe_bp.route('/usergroupe/migrate', methods=['POST'])
def migrate_promo() :
    try:
        data = request.json
        
        result = UserGroupeService.update_promo_etudiants(**data)
        
        if "error" in result:
            return jsonify({'error': result["error"]}), 403

        return jsonify({'message': result["message"]}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 403

