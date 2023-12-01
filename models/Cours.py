from database.config import db
from models.Ressources import Ressources
from models.Promotion import Promotion
from models.Groupe import Groupe
from models.Salle import Salle
from models.Teacher import Teacher


class Cours(db.Model):

    __tablename__= "cours"
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    heureDebut = db.Column(db.Time, nullable=False)
    heureFin = db.Column(db.Time, nullable=False)
    enseignant = db.Column(db.String(15), db.ForeignKey('staff.initial'))
    ressource = db.Column(db.String(64), db.ForeignKey('ressources.initial'))
    promotion = db.Column(db.String(64), db.ForeignKey('promotion.name'))
    groupe = db.Column(db.Integer, db.ForeignKey('groupe.id'), nullable=False)
    salle = db.Column(db.String(64), db.ForeignKey("salle.nom"))
    appelEffectue = db.Column(db.Boolean, nullable=True)
    absences = db.relationship('Absence', backref='cours', lazy='dynamic')

    def __init__(self, date, heureDebut, heureFin, enseignant_initial, ressource, promotion, groupe, salle, appelEffectue):
        self.date = date
        self.heureDebut = heureDebut
        self.heureFin = heureFin
        self.enseignant_initial = enseignant_initial
        self.ressource = ressource
        self.promotion = promotion
        self.groupe = groupe
        self.salle = salle
        self.appelEffectue = appelEffectue

    def appelFait(self, appelFait):
        self.appelEffectue = appelFait