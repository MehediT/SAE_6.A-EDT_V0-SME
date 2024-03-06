from models.relations.user_groupe import student_course_association
from database.config import db 
from services.UserGroupeService import UserGroupeService

dataEtudiantGroupe = [
    {
        "id_student": 1,
        "id_group": 10
    },
    {
        "id_student": 2,
        "id_group": 11
    },
    {
        "id_student": 3,
        "id_group": 12
    },
    {
        "id_student": 4,
        "id_group": 13
    },
    {
        "id_student": 5,
        "id_group": 14
    }
]


for etudiantGroupe in dataEtudiantGroupe:
    
    idStudent = etudiantGroupe["id_student"]
    idGroup = etudiantGroupe["id_group"]

    UserGroupeService.add_user_to_group(idStudent,idGroup)

