from database.config import db
# from models.Enseignant import Enseignant

class Disponibilite(db.Model):
  __tablename__ = "disponibilité"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  enseignant = db.Column(db.String(15), db.ForeignKey('enseignant.initial'))
  disponible = db.Column(db.Boolean, nullable=False)
  date_debut_disponibilite = db.Column(db.DateTime, nullable=False)
  date_fin_disponibilite = db.Column(db.DateTime, nullable=False)

  def __init__(self, enseignant, disponible, date_debut_disponibilite, date_fin_disponibilite):
    self.enseignant = enseignant
    self.disponible = disponible
    self.date_debut_disponibilite = date_debut_disponibilite
    self.date_fin_disponibilite = date_fin_disponibilite

  