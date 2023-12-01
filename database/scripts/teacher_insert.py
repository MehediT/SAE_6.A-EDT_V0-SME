from models.Teacher import Teacher
from database.config import db 
from services.TeacherService import TeacherService


dataTeacher = [

    {
        'name' : 'Philippe',
        'lastname' : 'Bonnot',
        'identifier' : 'philippe_bonnot',
        'password' : 'philippe1234'
    },

    {
        'name' : 'Jeremy',
        'lastname' : 'Marcinkowski',
        'identifier' : 'jeremy_marcinkowski',
        'password' : 'jeremy1234'
    },

    {
        'name' : 'Philippe',
        'lastname' : 'Bonnet',
        'identifier' : 'philippe_bonnet',
        'password' : 'philippe21234'
    }
]


for teacher in dataTeacher:
    TeacherService.create_teacher(teacher)
    

