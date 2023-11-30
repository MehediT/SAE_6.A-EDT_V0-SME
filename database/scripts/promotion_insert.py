from models.Promotion import Promotion
from database.config import db 
from services.PromotionService import PromotionService


dataPromotions = [
  {
    'name' : 'BUT INFO S5',
    'niveau' : 3
  },

  {
    'name' : 'BUT GACO S5',
    'niveau' : 3
  }

]

for promotion in dataPromotions:
    name = dataPromotions["name"]
    niveau = dataPromotions["niveau"]

    