from database.config import db
from models.Cours import Cours

class CoursService:

    @staticmethod
    def create_cours(date, heureDebut, heureFin, enseignant, ressource, promotion, groupe, salle):
        cours = Cours(date, heureDebut, heureFin, enseignant, ressource, promotion, groupe, salle, False)

        db.session.add(cours)
        db.session.commit()

        return cours
    
    @staticmethod
    def get_cours_by_groupe(groupe):
        return Cours.query.filter_by(groupe=groupe).all()
    
    @staticmethod
    def get_cours_by_promo(promo):
        return Cours.query.filter_by(promotion=promo).all()
    
    @staticmethod
    def get_teacher_schedule(enseignant):
        return Cours.query.filter_by(enseignant=enseignant).all()
    
    @staticmethod
    def get_salle_availability(salle):
        return Cours.query.filter_by(salle=salle).all()
    
    @staticmethod
    def get_cours_by_date(date):
        return Cours.query.filter_by(date=date).all()
    
    @staticmethod
    def get_cours_by_ressource(ressource):
        return Cours.query.filter_by(ressource=ressource).all()
    
    @staticmethod
    def set_groupe(idCours, new_groupe):
        cour_to_update = Cours.query.filter_by(id=idCours).first()

        cour_to_update.groupe=new_groupe
        db.session.commit()

    @staticmethod
    def set_promo(idCours, new_promo):
        cour_to_update = Cours.query.filter_by(id=idCours).first()

        cour_to_update.promotion=new_promo
        db.session.commit()

    @staticmethod
    def set_teacher(idCours, new_enseignant):
        cour_to_update = Cours.query.filter_by(id=idCours).first()

        cour_to_update.enseignant=new_enseignant
        db.session.commit()

    @staticmethod
    def set_salle(idCours, new_salle):
        cour_to_update = Cours.query.filter_by(id=idCours).first()

        cour_to_update.salle=new_salle
        db.session.commit()

    @staticmethod
    def set_date(idCours, new_date):
        cour_to_update = Cours.query.filter_by(id=idCours).first()

        cour_to_update.date=new_date
        db.session.commit()

    @staticmethod
    def set_ressource(idCours, new_ressource):
        cour_to_update = Cours.query.filter_by(id=idCours).first()

        cour_to_update.ressource=new_ressource
        db.session.commit()

    
    @staticmethod
    def delete_cour(id):
        cour = Cours.query.filter_by(id=id).first()
        
        db.session.delete(cour)
        db.session.commit() 
