from database.config import db
from models.ResponsableEdt import ResponsableEdt

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