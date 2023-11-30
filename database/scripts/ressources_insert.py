from models.Ressources import Ressources
from database.config import db 
from services.RessourcesService import RessourcesService


dataRessources = [

  {
    'initial' : 'R5.A.08',
    'name' : 'Qualité de dev',
    'promotion' : 'BUT INFO'
  },

  {
    'initial' : 'R5.A.12',
    'name' : 'Modélisations',
    'promotion' : 'BUT INFO'
  }
]


for ressource in dataRessources:
    initial = dataRessources["initial"]
    name = dataRessources["name"]
    promo = dataRessources["promotion"]

    RessourcesService.create_resource(name,initial,promo)