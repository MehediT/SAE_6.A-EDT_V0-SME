from models.Salle import Salle
from database.config import db 
from services.SalleService import SalleService



dataSalles = [

  {
  'nom' : 'A2-05',
  'ordi' : 32,
  'tableauNumerique' : 0,
  'videoProjecteur' : 1
  },

  {
  'nom' : 'B1-09',
  'ordi' : 20,
  'tableauNumerique' : 0,
  'videoProjecteur' : 1
  }

]


for salles in dataSalles:
    nom = salles["nom"]
    ordi = salles["ordi"]
    tableauNumerique = salles["tableauNumerique"]
    videoProjecteur = salles["videoProjecteur"]

    SalleService.create_salle(nom,ordi,tableauNumerique,videoProjecteur)

    