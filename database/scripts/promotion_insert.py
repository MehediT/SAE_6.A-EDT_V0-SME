from models.Promotion import Promotion
from database.config import db 
from services.PromotionService import PromotionService


dataPromotions = [
  {
    'name' : 'BUT INFO',
    'niveau' : 3,
    'id_resp' : 1
  },

  {
    'name' : 'BUT GACO',
    'niveau' : 3,
    'id_resp' : 2
  }

]

for promotion in dataPromotions:
    PromotionService.create_promo(promotion)
