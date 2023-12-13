import json
from models.Cours import Cours
from database.config import db 
from services.CoursService import CoursService
from datetime import date, time


date

dataCours = [
    {
    "start_time" : "2023-12-04 08:55:00",
    "end_time" : "2023-12-04 09:00:00",
    "initial_ressource" : "R5A05",
    "id_group":2,
    "id_enseignant":1,
    "name_salle":"A2-05"
  },

  {
    "start_time" : "2023-12-04 13:55:00",
    "end_time" : "2023-12-04 15:00:00",
    "initial_ressource" : "R5A05",
    "id_group":1,
    "id_enseignant":1,
    "name_salle":"B1-09"
  },

  {
    "start_time" : "2023-12-13 13:55:00",
    "end_time" : "2023-12-13 14:55:00",
    "initial_ressource" : "R5A05",
    "id_group":1,
    "id_enseignant":1
  }
]


for cours in dataCours:
    
    CoursService.create_course(cours)


