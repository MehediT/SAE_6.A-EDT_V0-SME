from models.EtudiantGroupe import EtudiantGroupe
from database.config import db 
from services.EtudiantGroupeService import EtudiantGroupeService

dataEtudiantGroupe = [

  {
    'id' : 1,
    'idEtudiant' : 'jonas_obrun',
    'idGroupe' : '2',
    'promotion' : 'BUT INFO'
  },

  {
    'id' : 2,
    'idEtudiant' : 'cyril_grosjean',
    'idGroupe' : '2',
    'promotion' : 'BUT INFO'
  },

  {
    'id' : 3,
    'idEtudiant' : 'nicolas_ramirez',
    'idGroupe' : '1',
    'promotion' : 'BUT INFO'
  }

]


for etudiantGroupe in dataEtudiantGroupe:
    idEtudiant = etudiantGroupe["idEtudiant"]
    idGroupe = etudiantGroupe["idGroupe"]

    EtudiantGroupeService.create_etudiant_groupe(idEtudiant,idGroupe)

