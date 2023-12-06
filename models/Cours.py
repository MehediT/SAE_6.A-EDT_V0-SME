from database.config import db
from models.Ressources import Ressources
from models.Groupe import Groupe
from models.Salle import Salle
from models.Teacher import Teacher


class Cours(db.Model):

    __tablename__= "cours"
    
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    initial_enseignant = db.Column(db.String(15), db.ForeignKey('staff.initial'), nullable=True)
    initial_ressource = db.Column(db.String(64), db.ForeignKey('ressources.initial'), nullable=False)
    id_group = db.Column(db.Integer, db.ForeignKey('groupe.id'), nullable=False)
    name_salle = db.Column(db.String(64), db.ForeignKey("salle.nom"), nullable=True)
    appelEffectue = db.Column(db.Boolean, nullable=False, default=False)
    # absences = db.relationship('Absence', backref='cours', lazy='dynamic')

    def __init__(self, start_time, end_time, initial_ressource, id_group, name_salle = None,initial_enseignant= None, **kwargs):
        self.start_time = start_time
        self.end_time = end_time
        self.initial_enseignant = initial_enseignant if initial_enseignant else db.null()
        self.initial_ressource = initial_ressource
        self.id_group = id_group
        self.name_salle = name_salle if name_salle else db.null()

    # def appelFait(self, appelFait):
    #     self.appelEffectue = appelFait

    def to_dict(self):
        return {
            'id': self.id,
            'start_time': self.start_time.strftime("%Y-%m-%d %H:%M:%S"),
            'end_time': self.end_time.strftime("%Y-%m-%d %H:%M:%S"),
            'initial_enseignant': self.initial_enseignant,
            'initial_ressource': self.initial_ressource,
            'id_group': self.id_group,
            'name_salle': self.name_salle,
            'appelEffectue': self.appelEffectue
        }
