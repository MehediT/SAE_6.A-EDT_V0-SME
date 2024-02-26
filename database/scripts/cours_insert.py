import json
from models.Cours import Cours
from database.config import db 
from services.CoursService import CoursService
from datetime import date, time


date

dataCours = [
    {
    "start_time" : "2024-02-21 08:00:00",
    "end_time" : "2024-02-21 09:00:00",
    "initial_ressource" : "R5A05",
    "id_group":1,
    "id_enseignant":1,
    "name_salle":"A2-05",
    "is_published":1
  }
]


for cours in dataCours:
    
    CoursService.create_course(cours)


