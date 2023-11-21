from database.config import db
from models.Promotion import Promotion

class Groupe(db.Model):
    __tablename__= "groupe"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    promotion = db.Column(db.String(64), db.ForeignKey('promotion.name'))
    groupeTd = db.Column(db.String(64), nullable=False)
    groupeTp = db.Column(db.String(64), nullable=True)
    cours = db.relationship('Cours', backref='groupe_assigne_cour', lazy='dynamic')

    def __init__(self, promo, groupeTd, groupeTp):
        self.promotion = promo
        self.groupeTd = groupeTd
        self.groupeTp = groupeTp
        