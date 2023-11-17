from database.config import db
from models.Groupe import Groupe
from models.Promotion import Promotion
from models.User import User 

class EtudiantGroupe(db.Model):
  __tablename__ = "etudiantgroupe"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  idEtudiant = db.Column(db.String(64), db.ForeignKey('user.identifier'))
  idGroupe = db.Column(db.Integer, db.ForeignKey('groupe.id'))
  promotion = db.Column(db.String(64), db.ForeignKey('promotion.name'))

  def __init__(self, idEtudiant, idGroupe, promo):
    self.idEtudiant = idEtudiant
    self.idGroupe = idGroupe
    self.promotion = promo