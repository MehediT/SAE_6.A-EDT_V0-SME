from database.config import db
from models.ResponsableEdt import ResponsableEdt
from services.AffiliationRespEdtService import AffiliationRespEdtService
from models.Staff import Staff
from models.User import User

class ResponsableEdtService():
    
    @staticmethod
    def get_all_responsable_edt():
      return ResponsableEdt.query.all()

    @staticmethod
    def create_responsable_edt(data):
        responsable_edt = ResponsableEdt(**data)
        db.session.add(responsable_edt)
        db.session.commit()

        return responsable_edt
    
    @staticmethod
    def get_by_id(id):
        return ResponsableEdt.query.filter_by(id_resp=id).first()
    
    @staticmethod
    def get_by_userId(userId):
        print(userId)
        respedt = ResponsableEdt.query.filter_by(id_staff=userId).first()
        print(respedt)
        return respedt
    
    @staticmethod
    def get_promos(respEdt):
        promos = AffiliationRespEdtService.get_promos_for_respedt(respEdt.id_resp)
        return promos
        # id_groups = [promo.id_group for promo in promos]
    

    @staticmethod
    def delete_responsable_edt(id):
        responsable_edt = ResponsableEdt.query.filter_by(id_resp=id).first()
        db.session.delete(responsable_edt)
        db.session.commit()
        return responsable_edt
    

    @staticmethod
    def update_responsableEdt(id, name: str, lastname: str, **kwargs):
        responsable_edt = ResponsableEdt.query.filter_by(id_resp=id).first()
        responsable_edt.name = name
        responsable_edt.lastname = lastname


        db.session.commit()
        return responsable_edt