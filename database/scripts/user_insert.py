from models.User import User
from database.config import db 
from services.UserService import UserService


dataUsers = [

  {
    'id' : 1,
    'userIdentifier' : 'jonas_obrun',
    'password' : 'jonas1234',
    'name' : 'Jonas',
    'lastname' : 'Obrun'
  },

  {
    'id' : 2,
    'userIdentifier' : 'cyril_grosjean',
    'password' : 'cyril1234',
    'name' : 'Cyril',
    'lastname' : 'Grosjean'
  },

  {
    'id' : 3,
    'userIdentifier' : 'nicolas_ramirez',
    'password' : 'nicolas1234',
    'name' : 'Nicolas',
    'lastname' : 'Ramirez'
  },

  {
    'id' : 4,
    'userIdentifier' : 'ismael_argence',
    'password' : 'ismael1234',
    'name' : 'Ismael',
    'lastname' : 'Argence'
  },

  {
    'id' : 5,
    'userIdentifier' : 'onur_genc',
    'password' : 'onur1234',
    'name' : 'Onur',
    'lastname' : 'Genc'
  },

]

for user in dataUsers:
    id = user["id"]
    userIdentifier = user["userIdentifier"]
    password = user["password"]
    name = user["name"]
    lastname = user["lastname"]

    UserService.create_user(userIdentifier,password,name,lastname,role="ROLE_STUDENT")

