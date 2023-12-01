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
    def get_promo_by_name(researched_promo_name):
        return Promotion.query.filter_by(name=researched_promo_name).first()
    
    
    @staticmethod
    def delete_promo(name):
        promo = Promotion.query.filter_by(name=name).first()
        db.session.delete(promo)
        db.session.commit()
        return promo
    
    @staticmethod
    def update_promo(name, niveau, **kwargs):
        promo = Promotion.query.filter_by(name=name).first()
        promo.niveau = niveau

        db.session.commit()
        return promo
    
