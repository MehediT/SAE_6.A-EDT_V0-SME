from models.Groupe import Groupe
from database.config import db 
from services.GroupeService import GroupeService

dataGroupes = []


for groupe in dataGroupes:
    GroupeService.create_groupe(groupe)