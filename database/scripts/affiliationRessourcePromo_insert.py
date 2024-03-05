from models.relations.ressource_promo import affiliation_ressource_promo
from database.config import db 
from services.AffRessourcePromoService import AffRessourcePromoService

data = [
    {
        "id_ressource" : "R5A08",
        "id_promo" : 1
    }
]

for aff in data:
    initial = data["id_ressource"]
    id_promo = data["id_promo"]
    AffRessourcePromoService.affiliate_ressource_to_promo(initial, id_promo)