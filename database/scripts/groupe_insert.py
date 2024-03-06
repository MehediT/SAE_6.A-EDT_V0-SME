from models.Groupe import Groupe
from database.config import db 
from services.GroupeService import GroupeService

dataGroupes = [
    {
      "name": "A",
      "id": 7,
      "id_group_parent": 1
    },
    {
      "name": "B",
      "id": 8,
      "id_group_parent": 1
    },
    {
      "name": "C",
      "id": 9,
      "id_group_parent": 1
    },
    {
      "name": "A1",
      "id": 10,
      "id_group_parent": 7
    },
    {
      "name": "A2",
      "id": 11,
      "id_group_parent": 7
    },
    {
      "name": "B1",
      "id": 12,
      "id_group_parent": 8
    },
    {
      "name": "B2",
      "id": 13,
      "id_group_parent": 8
    },
    {
      "name": "C1",
      "id": 14,
      "id_group_parent": 9
    },
    {
      "name": "C2",
      "id": 15,
      "id_group_parent": 9
    }
]


for groupe in dataGroupes:
    GroupeService.create_groupe(groupe)