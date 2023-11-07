from database.config import db
from models.Cours import Cours

class Groupe(db.Model):
    __tablename__= "groupe"

    idGroupe = db.Column(db.String(64), primary_key=True)
    promotion = db.Column(db.String(64), db.ForeignKey('Promotion.name'))
    cours = db.relationship('Cours', backref='groupe_name', lazy='dynamic')

    def __init__(self, idGroupe):
        self.idGroupe =idGroupe