from database.config import db
from models.Promotion import Promotion

class Ressources(db.Model):
    __tablename__= "ressources"

    initial = db.Column(db.String(5), primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    promo = db.Column(db.String(64), db.ForeignKey('promotion.name'))
    cours = db.relationship('Cours', backref='ressource_initial', lazy='dynamic')

    def __init__(self, name, initial, promo):
        self.name=name
        self.initial = initial
        self.promo = promo

    

    def to_dict(self):
        return {
            'initial': self.initial,
            'name': self.name,
            'promo': self.promo
        }

    
