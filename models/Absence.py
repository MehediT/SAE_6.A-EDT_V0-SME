from database.config import db 
from models.Cours import Cours
from models.User import User


class Absence(db.Model):
    __tablename__= "absence"

    idEtudiant = db.Column(db.String(80), db.ForeignKey('user.username'), primary_key=True)
    idCour = db.Column(db.Integer, db.ForeignKey('cours.id'), primary_key=True)
    justifiée = db.Column(db.Boolean)

    def __init__(self, idEtudiant, idCour):
        self.idEtudiant = idEtudiant
        self.idCour = idCour
        self.justifiée = False