from database.config import db
from models.Groupe import Groupe

class GroupeService:

    @staticmethod
    def create_groupe(data):
        groupe = Groupe(**data)
        db.session.add(groupe)
        db.session.commit()
        return groupe
    
    @staticmethod
    def get_all_groupes():
        return Groupe.query.all()
    
    @staticmethod
    def get_groupe_by_id(idGroupe):
        return Groupe.query.get(idGroupe)
    
    @staticmethod
    def delete_groupe(idGroupe):
        groupe = Groupe.query.get(idGroupe)

        db.session.delete(groupe)
        db.session.commit()

        return groupe

    @staticmethod
    def update_groupe(id, name):
        groupe = Groupe.query.get(id)
        groupe.name = name
        db.session.commit()
        return groupe

