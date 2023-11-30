from models.Cours import Cours
from database.config import db 
from services.CoursService import CoursService
from datetime import date, time



dataCours = [

  {

    'id': 1,
    'date' : date(2023,12,8),
    'heureDebut' : time(11,00,00) ,
    'heureFin' : time(12,00,00),
    'enseignant' : 'JEM',
    'ressource' : 'Qualité dev',
    'promotion' : 'BUT INFO S5',
    'groupe' : 1,
    'salle' : 'A2-05'
  },

  {
    'id': 2,
    'date' : date(2023,12,8),
    'heureDebut' : time(14,00,00),
    'heureFin' : time(15,30,00),
    'enseignant' : 'PB',
    'ressource' : 'Modélisations',
    'promotion' : 'BUT INFO S5',
    'groupe' : 2,
    'salle' : 'B1-09'
  }
]


for cours in dataCours:
    id = cours["id"]
    date = cours["date"]
    heureDebut = cours["heureDebut"]
    heureFin = cours["heureFin"]
    enseignant = cours["enseignant"]
    ressource = cours["ressource"]
    promotion = cours["promotion"]
    groupe = cours["groupe"]
    salle = cours["salle"]
    
    CoursService.create_cours(date, heureDebut, heureFin,enseignant, ressource,promotion, groupe, salle)


