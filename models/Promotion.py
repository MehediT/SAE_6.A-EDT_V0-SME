from database.config import db

class Promotion(db.Model):
    __tablename__= "promotion"

    name = db.Column(db.String(64), primary_key=True)
    niveau = db.Column(db.Integer, nullable=False)
    cours = db.relationship('Cours', backref='promotion_name', lazy='dynamic')
    groupes = db.relationship('Groupe', backref='from_promotion', lazy='dynamic')
    etudGrp = db.relationship('EtudiantGroupe', backref='promotions_groupes', lazy='dynamic')
    ressources = db.relationship('Ressources', backref='promo_ressources', lazy='dynamic')
    id_resp = db.Column(db.BigInteger, db.ForeignKey('responsable_edt.id_resp'))

    # respEdt_Promo = db.relationship('ReponsableEdt', backref='promos_of_respEdt', lazy='dynamic')

    def __init__(self, name, niveau, id_resp, **kwargs):
        self.name = name
        self.niveau = niveau
        self.id_resp = id_resp


    def to_dict(self):
        return {
            'name': self.name,
            'niveau': self.niveau,
            "id_resp": self.id_resp,
        }