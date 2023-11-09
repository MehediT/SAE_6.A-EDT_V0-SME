from database.config import db

class Teacher(db.Model):
    __tablename__= "teacher"

    id = db.Column(db.Integer, primary_key=True)
    initial_name = db.Column(db.String(80), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __init__(self, initial_name, user_id):
        self.initialName = initial_name
        self.user_id = user_id