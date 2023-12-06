from models.Promotion import Promotion
from database.config import db 
from services.PromotionService import PromotionService


dataPromotions = [
  {
    'niveau' : 3,
    'name' : 'BUT INFO S3'
  },

  {
    'niveau' : 2,
    'name' : 'BUT GACO S2'
  },

  {
    'niveau' : 5,
    'name' : 'BUT QLIO S5'
  }

]

for promotion in dataPromotions:
    PromotionService.create_promo(promotion)
