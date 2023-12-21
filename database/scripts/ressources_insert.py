from models.Ressources import Ressources
from database.config import db 
from services.RessourcesService import RessourcesService


dataRessources = [

  {
    'initial' : 'R5A08',
    'name' : 'Qualite de dev',
    'id_promo' : 2,
    'color':'0D3978'
  },

  {
    'initial' : 'R5A12',
    'name' : 'Modelisations',
    'id_promo' : 1,
    'color':'590D78'
  },

  {
    'initial' : 'R5A05',
    'name' : 'PPP',
    'id_promo' : 3,
    'color':'78650D'
  }
]


for ressource in dataRessources:
    RessourcesService.create_resource(ressource)