import json
from models.Cours import Cours
from database.config import db 
from services.CoursService import CoursService
from datetime import date, time


date

dataCours = [
    {
      "id": 1,
      "start_time": "2024-03-04 08:00:00",
      "end_time": "2024-03-04 10:00:00",
      "id_enseignant": 1,
      "initial_ressource": "R3-01",
      "id_group": 1,
      "name_salle": "B1-09",
      "appelEffectue": 0,
      "is_published": 1,
      "evaluation": 0
    },
    {
      "id": 2,
      "start_time": "2024-03-04 10:00:00",
      "end_time": "2024-03-04 11:00:00",
      "id_enseignant": 2,
      "initial_ressource": "R3-02",
      "id_group": 1,
      "name_salle": "B1-10",
      "appelEffectue": 0,
      "is_published": 1,
      "evaluation": 0
    },
    {
      "id": 3,
      "start_time": "2024-03-04 12:00:00",
      "end_time": "2024-03-04 14:00:00",
      "id_enseignant": 1,
      "initial_ressource": "R3-03",
      "id_group": 1,
      "name_salle": "B1-11",
      "appelEffectue": 0,
      "is_published": 1,
      "evaluation": 0
    },
    {
      "id": 4,
      "start_time": "2024-03-04 14:30:00",
      "end_time": "2024-03-04 16:00:00",
      "id_enseignant": 2,
      "initial_ressource": "R3-04",
      "id_group": 1,
      "name_salle": "B1-12",
      "appelEffectue": 0,
      "is_published": 1,
      "evaluation": 0
    },
    {
      "id": 5,
      "start_time": "2024-03-04 16:00:00",
      "end_time": "2024-03-04 17:30:00",
      "id_enseignant": 1,
      "initial_ressource": "R3-05",
      "id_group": 1,
      "name_salle": "B1-13",
      "appelEffectue": 0,
      "is_published": 1,
      "evaluation": 0
    },
    {
      "id": 6,
      "start_time": "2024-03-05 13:00:00",
      "end_time": "2024-03-05 15:00:00",
      "id_enseignant": 2,
      "initial_ressource": "R3-06",
      "id_group": 1,
      "name_salle": "B1-14",
      "appelEffectue": 0,
      "is_published": 1,
      "evaluation": 0
    },
    {
      "id": 7,
      "start_time": "2024-03-05 10:00:00",
      "end_time": "2024-03-05 12:00:00",
      "id_enseignant": 1,
      "initial_ressource": "R3-07",
      "id_group": 1,
      "name_salle": "B1-15",
      "appelEffectue": 0,
      "is_published": 1,
      "evaluation": 0
    },
    {
      "id": 8,
      "start_time": "2024-03-05 15:00:00",
      "end_time": "2024-03-05 17:00:00",
      "id_enseignant": 2,
      "initial_ressource": "R3-08",
      "id_group": 1,
      "name_salle": "B1-16",
      "appelEffectue": 0,
      "is_published": 1,
      "evaluation": 0
    },
    {
      "id": 9,
      "start_time": "2024-03-05 08:00:00",
      "end_time": "2024-03-05 10:00:00",
      "id_enseignant": 1,
      "initial_ressource": "R3-09",
      "id_group": 1,
      "name_salle": "B1-17",
      "appelEffectue": 0,
      "is_published": 1,
      "evaluation": 0
    },
    {
      "id": 10,
      "start_time": "2024-03-06 10:00:00",
      "end_time": "2024-03-06 12:00:00",
      "id_enseignant": 2,
      "initial_ressource": "R3-10",
      "id_group": 1,
      "name_salle": "B1-18",
      "appelEffectue": 0,
      "is_published": 1,
      "evaluation": 0
    }
]


for cours in dataCours:
    
    CoursService.create_course(cours)


