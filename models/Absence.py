from database.config import db 
from models.Cours import Cours


class Absence(db.Model):
    __tablename__= "absence"

    idEtudiant = db.Column(db.Integer, db.ForeignKey('User.identifier'), primary_key=True)
    idCour = db.Column(db.Integer, db.ForeignKey('Cours.id'), primary_key=True)
    justifiée = db.Column(db.Boolean)

    def __init__(self, idEtudiant, idCour):
        self.idEtudiant = idEtudiant
        self.idCour = idCour
        self.justifiée = False