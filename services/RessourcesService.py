from database.config import db
from models.Ressources import Ressources

class RessourcesService:

    @staticmethod
    def create_resource(name):
        resource = Ressources(name)
        db.session.add(resource)
        db.session.commit()
        return resource
    
    @staticmethod
    def get_all_ressources():
        ressources = Ressources.query.order_by(Ressources.name).all()

        ressources = row_to_dict(ressources)

        return ressources
    
    @staticmethod
    def add_ressource(name):
        return Ressources.query.get(name) is not None
    
    @staticmethod
    def delete_ressource(initial):
        resource = Ressources.query.filter_by(initial=intial).first()
        if resource is not None:
            db.session.delete(resource)
            db.session.commit
        else:
            print("Cette ressource n'existe pas.")

    def row_to_dict(row: Row) -> dict:
        """Converts a SQLAlchemy Row object to a Python dictionary."""

        try:
            columns = row.__table__.columns
        except AttributeError:
            columns = []

        return {col.name: getattr(row, col.name) for col in columns}