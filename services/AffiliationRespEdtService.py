from database.config import db
from models.relations.affiliation_resp_edt import affiliation_resp_edt

class AffiliationRespEdtService:

  @staticmethod
  def affiliate_respedt_to_promo(resp_id, promo_id):
    # Create an instance of the user_groupe table
    resp_edt_association = affiliation_resp_edt.insert().values(id_resp=resp_id, id_promo=promo_id)

    # Add the association to the database session
    db.session.execute(resp_edt_association)

    # Commit the changes to the database
    db.session.commit()


  @staticmethod
  def get_respedt_by_promo(idResp, idPromo):
    return affiliation_resp_edt.query.filter_by(id_Promo=idPromo).filter_by(id_Resp=idResp).all()
  
  @staticmethod
  def get_promos_for_respedt(idRespedt):
      query = db.session.query(affiliation_resp_edt).filter_by(id_resp=idRespedt)

      result = query.all()
      promos = [id_promo for id_resp, id_promo in result]

      return promos
  @staticmethod
  def get_promo_by_respedt(idResp, idPromo):
    return affiliation_resp_edt.query.filter_by(id_resp=idResp).filter_by(id_promo=idPromo).all()
  
  @staticmethod
  def delete_respEdt_promo(idResp):
    affiliation_resp_edt_delete = affiliation_resp_edt.query.filter_by(id_resp=idResp).first()

    db.session.delete(affiliation_resp_edt_delete)
    db.session.commit()