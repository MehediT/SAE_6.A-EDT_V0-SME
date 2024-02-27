from models.Ressources import Ressources
from database.config import db 
from services.RessourcesService import RessourcesService


dataRessources = []


for ressource in dataRessources:
    RessourcesService.create_resource(ressource)