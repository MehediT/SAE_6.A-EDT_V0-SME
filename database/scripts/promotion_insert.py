from models.Promotion import Promotion
from database.config import db 
from services.PromotionService import PromotionService


dataPromotions = [
  {
    'name' : 'BUT INFO',
    'niveau' : 3
  },

  {
    'name' : 'BUT GACO',
    'niveau' : 3
  }

]

for promotion in dataPromotions:
    nom = dataPromotions["name"]
    niveau = dataPromotions["niveau"]

    PromotionService.create_promo(nom,niveau)
