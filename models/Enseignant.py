from database.config import db
from models.Cours import Cours
from models.Disponibilite import Disponibilite
from models.User import User

class Enseignant(db.Model):
    __tablename__= "enseignant"

    id = db.Column(db.Integer, primary_key=True)
    initial_name = db.Column(db.String(80), unique=True, nullable=False)
    nb_heures_previsionnelles = db.Column(db.Integer, nullable=True)
    nb_heure_faites = db.Column(db.Integer, nullable=False)
    disponibilite = db.relationship('Disponibilite', backref='disponibilite_enseignant', lazy='dynamic')
    cours = db.relationship('Cours', backref='enseignant', lazy='dynamic')

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __init__(self, initial_name, user_id, nb_heures_previsionnelles):
        self.initialName = initial_name
        self.user_id = user_id
        self.nb_heures_previsionnelles = nb_heures_previsionnelles
        self.nb_heure_faites = 0

    