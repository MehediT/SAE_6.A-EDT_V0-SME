from models.RespEDTPromo import RespEDTPromo
from database.config import db 
from services.RespEDTPromoService import RespEDTPromoService


dataRespEDT = [

  {
    'id' : 1,
    'respEDT' : 'philippe_bonnot',
    'promotion' : 'BUT INFO'
  },

  {
    'id' : 2,
    'respEDT' : 'mec_random',
    'promotion' : 'BUT GACO'
  }
]


for resp in dataRespEDT:
    id = resp["id"]
    promo = resp["promotion"]
    respEDT = resp["respEDT"]

    RespEDTPromoService.create_respedt_promo(id,promo)


    