from database.config import db
from models.Promotion import Promotion

class PromotionService:

    @staticmethod
    def create_promo(data):
        promo = Promotion(**data)

        db.session.add(promo)
        db.session.commit()

        return promo
    
    @staticmethod
    def get_all_promos():
        return Promotion.query.all()
    
    @staticmethod
    def get_promo_by_id(id_promo):
        return Promotion.query.filter_by(id_promo=id_promo).first()
    
    
    @staticmethod
    def delete_promo(id_promo):
        promo = Promotion.query.filter_by(id_promo=id_promo).first()
        db.session.delete(promo)
        db.session.commit()
        return promo
    
    @staticmethod
    def update_promo(id_promo,name, niveau, id_resp, **kwargs):
        promo = Promotion.query.filter_by(id_promo=id_promo).first()
        promo.name = name
        promo.niveau = niveau
        promo.id_resp = id_resp

        db.session.commit()
        return promo
    