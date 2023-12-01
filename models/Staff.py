from database.config import db
from models.User import User

class Staff(User):
    __tablename__= "staff"

    id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True)
    initial = db.Column(db.String(80), unique=True, nullable=False)



    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = super().id
        self.initial = self.get_initial(self.name, self.lastname)
        # self.initial = initial


    def to_dict(self):
        print("here")
        return {
            'id': self.id,
            'initial': self.initial,
            'user' :super().to_dict()
        }
    
    def get_initial(self, name, lastname):
        def get_initial_from_part(part, index):
            return part[:index].upper()

        initial = get_initial_from_part(name, 1) + get_initial_from_part(lastname, 1)
        initialExist = self.get_by_initial(initial_name=initial)

        indexChar = 2

        while initialExist is not None:
            initial = ""

            for part in [name, lastname]:
                if indexChar <= len(part):
                    initial += part[:indexChar].upper()

            initialExist = self.get_by_initial(initial_name=initial)
            indexChar += 1

        return initial


    def get_by_initial(self,initial_name):
        staff = Staff.query.filter_by(initial=initial_name).first()
        return staff
    
    

    