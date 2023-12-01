from database.config import db
from models.Groupe import Groupe

class Ressources(db.Model):
    __tablename__= "ressources"

    initial = db.Column(db.String(5), primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    groupe = db.Column(db.Integer, db.ForeignKey('groupe.id'))
    cours = db.relationship('Cours', backref='ressource_initial', lazy='dynamic')

    def __init__(self, name, initial, groupe):
        self.name=name
        self.initial = initial
        self.groupe = groupe

    

    def to_dict(self):
        return {
            'initial': self.initial,
            'name': self.name,
            'groupe': self.groupe
        }

    
