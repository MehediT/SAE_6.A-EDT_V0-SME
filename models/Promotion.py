from database.config import db
from models.Cours import Cours

class Promotion(db.Model):
    __tablename__= "promotion"

    name = db.Column(db.String(64), primary_key=True)
    niveau = db.Column(db.Integer, nullable=False)
    cours = db.relationship('Cours', backref='promotion_name', lazy='dynamic')
    groupes = db.relationship('Groupe', backref='from_promotion', lazy='dynamic')

    def __init__(self, name):
        self.name = name