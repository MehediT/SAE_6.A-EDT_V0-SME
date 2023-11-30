from models.Absence import Absence
from database.config import db 
from services.AbsenceService import AbsenceService


absences = [
  {
  'userId' : 'jonas_obrun',
  'coursId': 1
  },

  {
  'userId' : 'cyril_grosjean',
  'coursId' : 2
  },

  {
  'userId' : 'nicolas_ramirez',
  'coursId': 2
  },

  {
  'userId' : 'onur_genc',
  'coursId': 1
  },

  {
  'userId' : 'ismael_argence',
  'coursId': 3
  }

]

for absence in absences:
    nom_absent = absence["userId"]
    id_absent = absence["coursId"]
    AbsenceService.create_absence(nom_absent,id_absent)






