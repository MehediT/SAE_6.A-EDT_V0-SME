from models.Groupe import Groupe
from database.config import db

class Promotion(Groupe):
    __tablename__= "promotion"

    id_promo = db.Column(db.Integer, primary_key=True)
    id_groupe = db.Column(db.Integer, db.ForeignKey('groupe.id', ondelete='CASCADE'), nullable=False)
    niveau = db.Column(db.Integer, nullable=False)
    id_resp = db.Column(db.BigInteger, db.ForeignKey('responsable_edt.id_resp', ondelete='CASCADE'))



    

    # cours = db.relationship('Cours', backref='groupe_assigne_cour', lazy='dynamic')

    def __init__(self,niveau,  id_group_parent = None, **kwargs):
        super().__init__(id_group_parent=id_group_parent, **kwargs)
        self.niveau = niveau

    def to_dict(self):
        return {
            'id': self.id_promo,
            'niveau': self.niveau,
            'group': super().to_dict(),
        }
        
        