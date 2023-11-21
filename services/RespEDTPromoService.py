from database.config import db
import json
from models.RespEDTPromo import RespEDTPromo
from models.User import User

class RespEDTPromoService():

  @staticmethod
  def create_respedt_promo(resp_id, promo):
    respedt_exist = User.query.filter_by(identifier=resp_id).first()

    if respedt_exist is not None:
      respedt_promo = RespEDTPromo(idRespEDT=resp_id, promoName=promo)

      db.session.add(respedt_promo)
      db.session.commit()

      return respedt_promo

    else:
      return "Le responsable d'emploi du temps spécifié n'existe pas..."
    
  @staticmethod
  def get_by_id(id):
    return RespEDTPromo.query.filter_by(id=id).first()
    
  @staticmethod
  def get_promo_by_respedt(resp_id):
    return RespEDTPromo.query(RespEDTPromo.promotion).filter_by(respEdt=resp_id).first()
  
  @staticmethod
  def get_respedt_by_edt(promoName):
    return RespEDTPromo.query(RespEDTPromo.respEdt).filter_by(promotion=promoName).first()
  
  @staticmethod
  def delete_respedtpromo(resp_id, promo):
    resp_to_delete = RespEDTPromo.query.filter_by(respEdt=resp_id).filter_by(promotion=promo).first()

    db.session.delete(resp_to_delete)
    db.session.commit()

    