from database.config import db
from models.User import User

class Staff(User):
    __tablename__= "staff"

    id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True)
    initial = db.Column(db.String(80), unique=True, nullable=False)



    def __init__(self, initial, **kwargs):
        super().__init__(**kwargs)
        self.id = super().id
        self.initial = kwargs.get('initial', "PB")
        # self.initial = initial


    def to_dict(self):
        print("here")
        return {
            'id': self.id,
            'initial': self.initial,
            'user' :super().to_dict()
        }

    