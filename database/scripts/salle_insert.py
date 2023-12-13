from models.Salle import Salle
from database.config import db 
from services.SalleService import SalleService



dataSalles = [

  {
  'name' : 'A2-05',
  'ordi' : 32,
  'tableauNumerique' : 0,
  'videoProjecteur' : 1
  },

  {
  'name' : 'B1-09',
  'ordi' : 20,
  'tableauNumerique' : 0,
  'videoProjecteur' : 1
  }

]


for salles in dataSalles:



    SalleService.create_salle(salles)

    