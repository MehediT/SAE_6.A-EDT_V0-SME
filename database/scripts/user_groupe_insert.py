from models.relations.user_groupe import student_course_association
from database.config import db 
from services.UserGroupeService import UserGroupeService

dataEtudiantGroupe = [

  {
    'id_student' : 1,
    'id_group' : 2,
  },

  {
    'id_student' : 2,
    'id_group' : 1,
  },

  {
    'id_student' : 3,
    'id_group' : 3
  }

]


for etudiantGroupe in dataEtudiantGroupe:
    
    idStudent = etudiantGroupe["id_student"]
    idGroup = etudiantGroupe["id_group"]

    UserGroupeService.add_user_to_group(idStudent,idGroup)

