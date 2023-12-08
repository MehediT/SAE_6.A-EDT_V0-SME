import json
from models.Cours import Cours
from database.config import db 
from services.CoursService import CoursService
from datetime import date, time


date

dataCours = [
    {
    "start_time" : "2023-12-06 12:55:00",
    "end_time" : "2023-12-06 14:00:00",
    "initial_ressource" : "R5A05",
    "id_group":2,
    "id_enseignant":1,
    "name_salle":"A2-05"
  },

  {
    "start_time" : "2023-12-06 13:55:00",
    "end_time" : "2023-12-06 15:00:00",
    "initial_ressource" : "R5A05",
    "id_group":1,
    "id_enseignant":1,
    "name_salle":"B1-09"
  },

  {
    "start_time" : "2023-12-06 12:55:00",
    "end_time" : "2023-12-06 13:00:00",
    "initial_ressource" : "R5A05",
    "id_group":1,
    "id_enseignant":1
  }
]


for cours in dataCours:
    
    CoursService.create_course(cours)


