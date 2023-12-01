from database.config import db
from models.Staff import Staff

from models.Promotion import Promotion

class ResponsableEdt(Staff):
  __tablename__ = "responsable_edt"
  id_resp = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
  id_user = db.Column(db.Integer, db.ForeignKey('staff.id', ondelete='CASCADE'))
  promotions = db.relationship('Promotion', backref='responsable_edt', lazy='dynamic')
  



  def __init__(self,role="ROLE_RESP_EDT", **kwargs):
    super().__init__(role=role,**kwargs)
    self.id = super().id

  def to_dict(self):
    return {
        'id': self.id_resp,
        'staff':super().to_dict(),
    }