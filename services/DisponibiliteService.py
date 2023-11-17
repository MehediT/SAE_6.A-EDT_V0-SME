from database.config import db
from models.Disponibilite import Disponibilite

class DisponibiliteService(db.model):

  @staticmethod
  def create_disponibilite(enseignant, disponible, date_debut_disponibilite, date_fin_disponibilite):
    disponibilite = Disponibilite(enseignant=enseignant, disponible=disponible, date_debut_disponibilite=date_debut_disponibilite, date_fin_disponibilite=date_fin_disponibilite)

    db.session.add(disponibilite)
    db.session.commit()

  @staticmethod
  def get_enseignant_disponibilite(initial_enseignant):
    return Disponibilite.query.filter_by(enseignant=initial_enseignant).first()
  
  @staticmethod
  def delete_disponibilite(initial_enseignant, date_debut_disponibilite, date_fin_disponibilite):
    disponibilite_to_delete = Disponibilite.query.filter_by(enseignant=initial_enseignant, date_debut_disponibilite=date_debut_disponibilite, date_fin_disponibilite=date_fin_disponibilite).first()

    db.session.delete(disponibilite_to_delete)
    db.session.commit()