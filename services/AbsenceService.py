from database.config import db 
from models.Absence import Absence

class AbsenceService:

    @staticmethod
    def get_all_absences(idEtudiant):
        return Absence.query.filter_by(idEtudiant=idEtudiant).all()
    
    @staticmethod
    def create_absence(idEtudiant, idCours):
        absence = Absence(idEtudiant, idCours)

        db.session.add(absence)
        db.session.commit()

        return absence
    
    @staticmethod
    def justify_absence(idEtudiant, idCours):
        absence_to_justify = Absence.query.filter_by(idEtudiant=idEtudiant, idCour=idCours).first()

        absence_to_justify.justifée = True

        db.session.commit()

    @staticmethod
    def delete_absence(idEtudiant, idCours):
        absence_to_delete = Absence.query.filter_by(idEtudiant=idEtudiant, idCour=idCours).first()
        db.session.delete(absence_to_delete)
        db.session.commit()

    @staticmethod
    def modify_absence(idEtudiant, idCours, newIdCours):
        absence_to_correct = Absence.query.filter_by(idEtudiant=idEtudiant, idCour=idCours).first()
        absence_to_correct.idCour = newIdCours
        db.session.commit()
