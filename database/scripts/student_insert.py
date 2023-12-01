from models.User import User
from database.config import db 
from services.StudentService import StudentService


dataUsers = [

  {
    'identifier' : 'jonas_obrun',
    'password' : 'jonas1234',
    'name' : 'Jonas',
    'lastname' : 'Obrun'
  },

  {
    'identifier' : 'cyril_grosjean',
    'password' : 'cyril1234',
    'name' : 'Cyril',
    'lastname' : 'Grosjean'
  },

  {
    'identifier' : 'nicolas_ramirez',
    'password' : 'nicolas1234',
    'name' : 'Nicolas',
    'lastname' : 'Ramirez'
  },

  {
    'identifier' : 'ismael_argence',
    'password' : 'ismael1234',
    'name' : 'Ismael',
    'lastname' : 'Argence'
  },

  {
    'identifier' : 'onur_genc',
    'password' : 'onur1234',
    'name' : 'Onur',
    'lastname' : 'Genc'
  },

]

for user in dataUsers:
    StudentService.create_student(user)

