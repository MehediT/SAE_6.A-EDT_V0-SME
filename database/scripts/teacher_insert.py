from models.Teacher import Teacher
from database.config import db 
from services.TeacherService import TeacherService


dataTeacher = [

    {
        'name' : 'Philippe',
        'lastname' : 'Bonnot',
        'username' : 'philippe_bonnot',
        'password' : 'philippe1234'
    },

    {
        'name' : 'Jeremy',
        'lastname' : 'Marcinkowski',
        'username' : 'jeremy_marcinkowski',
        'password' : 'jeremy1234'
    },

    {
        'name' : 'Philippe',
        'lastname' : 'Bonnet',
        'username' : 'philippe_bonnet',
        'password' : 'philippe21234'
    }
]


for teacher in dataTeacher:
    TeacherService.create_teacher(teacher)
    

