from models.Ressources import Ressources
from database.config import db 
from services.RessourcesService import RessourcesService


dataRessources = [

  {
    'initial' : 'R5A08',
    'name' : 'Qualite de dev',
    'promo' : 'BUT INFO'
  },

  {
    'initial' : 'R5A12',
    'name' : 'Modelisations',
    'promo' : 'BUT INFO'
  }
]


for ressource in dataRessources:
    RessourcesService.create_resource(ressource)