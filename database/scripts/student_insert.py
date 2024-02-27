from models.User import User
from database.config import db 
from services.StudentService import StudentService


dataUsers = []

for user in dataUsers:
    StudentService.create_student(user)

