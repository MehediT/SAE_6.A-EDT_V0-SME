from models.Groupe import Groupe
from database.config import db 
from services.GroupeService import GroupeService

dataGroupes = [

  {
    'niveau' : 3,
    'name' : 'BUT INFO S3',
    'id_group_parent' : 1
  },

  {
    'niveau' : 2,
    'name' : 'BUT GACO S2',
    'id_group_parent' : 1
  },

  {
    'niveau' : 5,
    'name' : 'BUT QLIO S5',
    'id_group_parent' : 1
  },

  {
    'niveau' : 2,
    'name' : 'BUT GACO S2',
    'id_group_parent' : 2
  }
]


for groupe in dataGroupes:
    GroupeService.create_groupe(groupe)