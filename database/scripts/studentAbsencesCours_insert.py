from models.relations.student_absences import student_absences_cours
from database.config import db 
from services.StudentAbsencesCoursService import StudentAbsencesCoursService


dataStudentAbsencesCours = [

    {
        'id_student' : 1,
        'id_cours' : 1

    },

    {
        'id_student' : 2,
        'id_cours' : 1
    },

    {
        'id_student' : 3,
        'id_cours' : 2
    },

    {
        'id_student' : 4,
        'id_cours' : 3
    },

    {
        'id_student' : 5,
        'id_cours' : 3
    }
]


for student_absences_cours in dataStudentAbsencesCours:

    idStudent = student_absences_cours["id_student"]
    idCours = student_absences_cours["id_cours"]
    StudentAbsencesCoursService.add_absence_to_cours(idStudent,idCours)
