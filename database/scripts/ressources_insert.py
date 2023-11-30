from models.Ressources import Ressources
from database.config import db 
from services.RessourcesService import RessourcesService


dataRessources = [

  {
    'initial' : 'R5A08',
    'name' : 'Qualite de dev',
    'promotion' : 'BUT INFO'
  },

  {
    'initial' : 'R5A12',
    'name' : 'Modelisations',
    'promotion' : 'BUT INFO'
  }
]


for ressource in dataRessources:
    initial = dataRessources["initial"]
    name = dataRessources["name"]
    promo = dataRessources["promotion"]

    RessourcesService.create_resource(name,initial,promo)