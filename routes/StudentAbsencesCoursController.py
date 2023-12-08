from flask import Blueprint, jsonify, request
from services.StudentAbsencesCoursService import StudentAbsencesCoursService

studentAbsences_bp = Blueprint('studentAbsencesCours', __name__)



@studentAbsences_bp.route('/studentAbsenceCours', methods=['POST'])
def add_student_absence_to_cours():

    idStudent = request.json["id_student"]
    idCours = request.json["id_cours"]
    
    try:
        # Associer un respEdt à une promo
        studentsAbsenceToCours = StudentAbsencesCoursService.add_absence_to_cours(idStudent,idCours)

        return jsonify(studentAbsences_bp.to_dict()),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403


@studentAbsences_bp.route('/studentAbsenceCours/getStudentByCours/<idCours>/<idStudent>', methods=['GET'])
def get_student_absences_by_cours(idCours,idStudent):
    
    try:
        # Récuperer un student avec un cours
        studentsAbsenceToCours = StudentAbsencesCoursService.get_student_absences_by_cours(idCours,idStudent)

        return jsonify(studentsAbsenceToCours.to_dict()),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403



@studentAbsences_bp.route('/studentAbsenceCours/getCoursByStudent/<idStudent>/<idCours>', methods=['GET'])
def get_cours_by_student_absences(idCours,idStudent):
    
    try:
        # Récuperer un cours avec un student
        studentsAbsenceToCours = StudentAbsencesCoursService.get_cours_by_student_absences(idCours,idStudent)

        return jsonify(studentsAbsenceToCours.to_dict()),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403


@studentAbsences_bp.route('/studentAbsenceCours/delete/<idStudent>/<idCours>', methods=['DELETE'])
def delete_absences_cours(idStudent,idCours):
    
    try:
        # Supprimer l'absence d'un student pour un cours spécifique
        studentsAbsenceToCours = StudentAbsencesCoursService.delete_absences_cours(idStudent,idCours)

        if not studentsAbsenceToCours:
            return jsonify({'error': 'Student and Cours not found'}),403

        return jsonify(studentsAbsenceToCours.to_dict()),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403

