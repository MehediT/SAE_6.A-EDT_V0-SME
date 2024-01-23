from models.Groupe import Groupe
from database.config import db

# Le modèle Promotion représente une promotion d'étudiants associée à un niveau d'étude (semestre)
class Promotion(Groupe):
    __tablename__= "promotion"

    # Clé primaire : ID de la promotion
    id_promo = db.Column(db.Integer, primary_key=True)
    id_groupe = db.Column(db.Integer, db.ForeignKey('groupe.id', ondelete='CASCADE'), nullable=False)
    # Niveau du semestre (exemple pour le BUT INFORMATIQUE Semestre 5 : 5)    
    niveau = db.Column(db.Integer, nullable=False)
    #id_resp = db.Column(db.BigInteger, db.ForeignKey('responsable_edt.id_resp', ondelete='CASCADE'), nullable=False)



    

    # cours = db.relationship('Cours', backref='groupe_assigne_cour', lazy='dynamic')
    
    # Constructeur de la classe Promotion
    def __init__(self, niveau, id_group_parent = None, **kwargs):
        super().__init__(id_group_parent=id_group_parent, **kwargs)
        self.niveau = niveau
        #self.id_resp = id_resp

    # Convertit l'objet Promotion en un dictionnaire
    def to_dict(self):
        return {
            'id': self.id_promo,
            'niveau': self.niveau,
            #'id_resp': self.id_resp,
            'group': super().to_dict(),
        }
        
        