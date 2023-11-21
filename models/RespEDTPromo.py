from database.config import db
from models.User import User
from models.Promotion import Promotion

class RespEDTPromo(db.Model):
  __tablename__ = "respEDTPromo"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  respEdt = db.Column(db.String(64), db.ForeignKey('user.identifier'))
  promotion = db.Column(db.String(64), db.ForeignKey('promotion.name'))

  def __init__(self, idRespEDT, promoName):
    self.RespEdt = idRespEDT
    self.Promotion = promoName