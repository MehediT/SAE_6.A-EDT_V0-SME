from database.config import db
from models.Cours import Cours

class CoursService:

    @staticmethod
    def create_course(data):
        course = Cours(**data)
        db.session.add(course)
        db.session.commit()
        return course
    
    def get_course_by_id(id):
        return Cours.query.get(id)
    
    @staticmethod
    def get_all_courses():
        courses = Cours.query.all()
        return courses
    
    @staticmethod
    def add_course(name):
        return Cours.query.get(name) is not None
    
    @staticmethod
    def delete_course(id):
        resource = Cours.query.get(id)
        return resource
    
    @staticmethod
    def update_course(id, start_time, end_time, initial_ressource, id_group, name_salle = None,initial_enseignant= None, **kwargs):
        course = Cours.query.get(id)

        course.start_time = start_time
        course.end_time = end_time
        course.initial_enseignant = initial_enseignant if initial_enseignant else db.null()
        course.initial_ressource = initial_ressource
        course.id_group = id_group
        course.name_salle = name_salle if name_salle else db.null()
        
        db.session.commit()
        return course
    

