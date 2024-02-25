from models.Groupe import Groupe
from database.config import db 
from services.GroupeService import GroupeService

dataGroupes = [

  {
    'niveau' : 3,
    'name' : 'Groupe B',
    'id_group_parent' : 1
  },

  {
    'niveau' : 3,
    'name' : 'Groupe A',
    'id_group_parent' : 1
  },

  {
    'niveau' : 3,
    'name' : 'Groupe B1',
    'id_group_parent' : 5
  },

  {
    'niveau' : 3,
    'name' : 'Groupe B2',
    'id_group_parent' : 5
  },

  {
    'niveau' : 2,
    'name' : 'Groupe A',
    'id_group_parent' : 2
  },

  {
    'niveau' : 5,
    'name' : 'Groupe C',
    'id_group_parent' : 3
  },

  {
    'niveau' : 2,
    'name' : 'Groupe A2',
    'id_group_parent' : 6
  }
]


for groupe in dataGroupes:
    GroupeService.create_groupe(groupe)