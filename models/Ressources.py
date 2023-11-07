from database.config import db
from models.Cours import Cours

class Ressources(db.Model):
    __tablename__= "ressources"

    initial = db.Column(db.String(5), primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    cours = db.relationship('Cours', backref='ressource_initial', lazy='dynamic')

    def __init__(self, name):
        self.name=name
        self.initial = Ressources.set_initial(name)

    def set_initial(name):
        namelist = name.split(" ")
        initial=""

        if namelist.length>1:
            for c in namelist:
                initial+=c[0]
        else:
            initial+=name[0]+name[1]

        return initial

    
