from models.Groupe import Groupe
from database.config import db 
from services.GroupeService import GroupeService

dataGroupes = [

  {
    'id' : 1,
    'promotion' : 'BUT INFO',
    'groupeTd' : 'groupe A',
    'groupeTp' : 'groupe A1'
  },

  {
    'id' : 2,
    'promotion' : 'BUT INFO',
    'groupeTd' : 'groupe A',
    'groupeTp' : 'groupe A2'
  },

  {
    'id' : 3,
    'promotion' : 'BUT GACO',
    'groupeTd' : 'groupe A',
    'groupeTp' : 'groupe A1'
  },

  {
    'id' : 4,
    'promotion' : 'BUT GACO',
    'groupeTd' : 'groupe A',
    'groupeTp' : 'groupe A2'
  }
]


for groupe in dataGroupes:
    id = groupe["id"]
    promo = groupe["promotion"]
    groupeTd = groupe["groupeTd"]
    groupeTp = groupe["groupeTp"]

    GroupeService.create_groupe(id,promo)