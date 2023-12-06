from database.config import db
from models.Disponibilite import Disponibilite

class DisponibiliteService():

  @staticmethod
  def create_disponibilite(data):
    disponibilite = Disponibilite(**data)

    db.session.add(disponibilite)
    db.session.commit()

  @staticmethod
  def get_enseignant_disponibilite(initial_enseignant):
    return Disponibilite.query.filter_by(enseignant=initial_enseignant).first()
  
  @staticmethod
  def delete_disponibilite(id):
    disponibilite_to_delete = Disponibilite.query.filter_by(id=id).first()

    db.session.delete(disponibilite_to_delete)
    db.session.commit()