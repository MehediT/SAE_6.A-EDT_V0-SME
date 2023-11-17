from database.config import db
from models.Promotion import Promotion

class PromotionService:

    @staticmethod
    def create_promo(name, niveau):
        promo = Promotion(name=name, niveau=niveau)

        db.session.add(promo)
        db.session.commit()

        return promo
    
    @staticmethod
    def get_all_promos():
        return Promotion.query().all()
    
    @staticmethod
    def get_promo_by_name(researched_promo_name):
        return Promotion.query().filter_by(name=researched_promo_name).first()
    
    @staticmethod
    def get_all_promos_by_niveau(niveau):
        return Promotion.query().filter_by(niveau=niveau).all()
    
    @staticmethod
    def delete_promo(name):
        promo = PromotionService.get_promo_by_name(name)
        db.session.delete(promo)
        db.session.commit()
    
