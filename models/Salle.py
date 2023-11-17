from database.config import db

class Salle(db.Model):
    __tablename__= "salle"

    nom = db.Column(db.String(64), primary_key=True)
    ordi = db.Column(db.Integer, nullable=True)
    tableauNumerique = db.Column(db.Integer, nullable=True)
    videoProjecteur = db.Column(db.Integer, nullable=True)
    cours = db.relationship('Cours', backref='salle_name', lazy='dynamic')


    def __init__(self, name, ordi, tableauNumerique, videoProjecteur):
        self.nom = name
        self.ordi = ordi
        self.tableauNumerique = tableauNumerique
        self.videoProjecteur = videoProjecteur