from database.config import db
from models.relations.ressource_promo import affiliation_ressource_promo
from models import Ressources
from models import Promotion

class AffiliationRessourcePromo:

    @staticmethod
    def affiliate_ressource_to_promo(idRessource, idPromo):
        asso = affiliation_ressource_promo.insert().values(id_ressource = idRessource, id_promo = idPromo)
        db.session.execute(asso)
        db.session.commit()

    @staticmethod
    def get_ressources_by_promo(idPromo):
        query = db.session.query(Ressources).join(affiliation_ressource_promo).join(Promotion).filter(Promotion.id_promo == idPromo)
        ressources = query.all()
        return ressources
    
    @staticmethod
    def get_promo_by_ressource(idRessource):
        query = db.session.query(Promotion).join(affiliation_ressource_promo).join(Ressources).filter(Ressources.initial == idRessource)
        promotions = query.all()
        return promotions
    
    @staticmethod
    def delete_affiliation(idRessource, idPromo):
        affiliation_ressource_promo.delete().where(
            (affiliation_ressource_promo.c.id_ressource == idRessource) &
            (affiliation_ressource_promo.c.id_promo == idPromo)
        )
        db.session.commit()