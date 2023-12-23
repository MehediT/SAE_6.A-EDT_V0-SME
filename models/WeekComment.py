from database.config import db
# from models.Enseignant import Enseignant

class WeekComment(db.Model):
    __tablename__ = "week_comment"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    week_number = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String(255), nullable=False)

    def __init__(self, week_number, year, content):
        self.week_number = week_number
        self.year = year
        self.content = content

    def to_dict(self):
        return {
            'id': self.id,
            'week_number': self.week_number,
            'year': self.year,
            'content': self.content
        }
        
  