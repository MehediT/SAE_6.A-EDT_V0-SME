from database.config import db
from models.Staff import Staff

class Teacher(Staff):
    __tablename__= "teacher"

    id = db.Column(db.Integer, db.ForeignKey('staff.id', ondelete='CASCADE'), primary_key=True)
    nb_heures_previsionnelles = db.Column(db.Integer, nullable=True)
    nb_heure_effectue = db.Column(db.Integer, nullable=False, default=0)
    disponibilite = db.relationship('Disponibilite', backref='disponibilite_enseignant', lazy='dynamic')
    cours = db.relationship('Cours', backref='enseignant_id', lazy='dynamic')


    def __init__(self,role="ROLE_TEACHER", **kwargs):
        super().__init__(role=role,**kwargs)
        self.id = super().id


    def to_dict(self):
        print("here")
        return {
            'id': self.id,
            'staff' :super().to_dict()
        }

    