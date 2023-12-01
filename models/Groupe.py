from database.config import db

class Groupe(db.Model):
    __tablename__= "groupe"

    name = db.Column(db.String(64))
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_group_parent = db.Column(db.Integer, db.ForeignKey('groupe.id', ondelete='CASCADE'), nullable=True)


    

    # cours = db.relationship('Cours', backref='groupe_assigne_cour', lazy='dynamic')

    def __init__(self, name, id_group_parent, **kwargs):
        if id_group_parent: 
            if Groupe.query.get(id_group_parent) == None:
                raise Exception("Groupe parent does not exist")
        else:
            id_group_parent = db.null()

        self.name = name
        self.id_group_parent = id_group_parent

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'id_group_parent': self.id_group_parent,
        }
        