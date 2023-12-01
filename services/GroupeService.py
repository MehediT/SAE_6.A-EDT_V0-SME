from database.config import db
from models.Groupe import Groupe

class GroupeService:

    @staticmethod
    def create_groupe(idGroupe, promo):
        groupe = Groupe(idGroupe=idGroupe, promotion=promo)
        db.session.add(groupe)
        db.session.commit()
        return groupe
    
    @staticmethod
    def get_all_groupes():
        return Groupe.query().all()
    
    @staticmethod
    def get_groupes_by_promo(from_promo):
        return Groupe.query().filter_by(promotion=from_promo).all()
    
    @staticmethod
    def get_groupe_by_id(idGroupe):
        return Groupe.query().filter_by(idGroupe=idGroupe).first()
    
    @staticmethod
    def delete_group(idGroupe):
        groupe = GroupeService.get_groupe_by_id(idGroupe)

        db.session.delete(groupe)
        db.session.commit()

    @staticmethod
    def update_groupe(id, promo, groupeTd, groupeTp):
        groupe = Groupe.query.get(id)
        groupe.promo = promo
        groupe.groupeTd = groupeTd
        groupe.groupeTp = groupeTp
        db.session.commit()
        return groupe

