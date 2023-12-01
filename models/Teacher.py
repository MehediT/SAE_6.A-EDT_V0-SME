from database.config import db
from models.User import User

class Teacher(User):
    __tablename__= "teacher"

    id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True)
    initial = db.Column(db.String(80), unique=True, nullable=False)
    nb_heures_previsionnelles = db.Column(db.Integer, nullable=True)
    nb_heure_effectue = db.Column(db.Integer, nullable=False, default=0)
    disponibilite = db.relationship('Disponibilite', backref='disponibilite_enseignant', lazy='dynamic')
    cours = db.relationship('Cours', backref='enseignant_id', lazy='dynamic')


    def __init__(self, initial,role="ROLE_TEACHER", **kwargs):
        super().__init__(role=role,**kwargs)
        self.user_id = super().id
        self.initial = initial


    def to_dict(self):
        print("here")
        return {
            'id': self.id,
            'initial': self.initial,
            'user' :super().to_dict()
        }

    