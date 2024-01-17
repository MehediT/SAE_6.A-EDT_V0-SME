from database.config import db
from models.Groupe import Groupe

class Ressources(db.Model):
    __tablename__= "ressources"

    initial = db.Column(db.String(5), primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    id_promo = db.Column(db.Integer, db.ForeignKey('promotion.id_promo'), nullable=False)
    cours = db.relationship('Cours', backref='ressource_initial', lazy='dynamic')
    color = db.Column(db.String(64), nullable=False)


    def __init__(self, name, initial, id_promo, color,  **kwargs):
        self.name=name
        self.initial = initial
        self.id_promo = id_promo
        self.color = color

    

    def to_dict(self):
        return {
            'initial': self.initial,
            'name': self.name,
            'id_promo': self.id_promo,
            'color':self.color
        }

    
