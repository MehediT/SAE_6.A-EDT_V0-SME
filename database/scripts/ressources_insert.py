from models.Ressources import Ressources
from database.config import db 
from services.RessourcesService import RessourcesService


dataRessources = [
    {
    'initial' : 'R5A08',
    'name' : 'Qualite de dev',
    'color':'0D3978'
    },
]


for ressource in dataRessources:
    RessourcesService.create_resource(ressource)