from models.Disponibilite import Disponibilite
from database.config import db 
from services.DisponibiliteService import DisponibiliteService
from datetime import datetime

dataDisponibilite = [

    {
        'enseignant' : 'BD',
        'disponible' : True,
        'date_debut_disponibilite' : datetime(2023,12,8,11,00,00),
        'date_fin_disponibilite' : datetime(2023,12,8,12,00,00)
    },

    {
        'enseignant' : 'JM',
        'disponible' : False,
        'date_debut_disponibilite' : datetime(2023,12,11,14,30,00),
        'date_fin_disponibilite' : datetime(2023,12,11,15,45,00)
    },

    {
        'enseignant' : 'PB',
        'disponible' : False,
        'date_debut_disponibilite' : datetime(2023,12,23,9,30,00),
        'date_fin_disponibilite' : datetime(2023,12,23,12,00,00)
    },

]


for disponibilite in dataDisponibilite:
    DisponibiliteService.create_disponibilite(disponibilite)