from database.config import db 
from models.Cours import Cours
from models.Student import Student


class Absence(db.Model):
    __tablename__= "absence"

    idEtudiant = db.Column(db.BigInteger, db.ForeignKey('student.id_student'), primary_key=True)
    idCour = db.Column(db.Integer, db.ForeignKey('cours.id'), primary_key=True)
    justifiée = db.Column(db.Boolean)

    def __init__(self, idEtudiant, idCour):
        self.idEtudiant = idEtudiant
        self.idCour = idCour
        self.justifiée = False