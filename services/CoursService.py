from operator import and_

from database.config import db
from models.Cours import Cours
from datetime import datetime, timedelta

from services.GroupeService import GroupeService

class CoursService:

    @staticmethod
    def create_course(data):

        resp, code = CoursService.can_create_course(**data)
        if code >= 400:
            return resp, code

        course = Cours(**data)
        
        db.session.add(course)
        db.session.commit()

        result = course.to_dict()
        if code > 200:
            result.update(resp)
            return result, code

        return course, 200
    
    def get_course_by_id(id):
        return Cours.query.get(id)
    
    @staticmethod
    def get_all_courses(args, publish: bool= None):

        query = Cours.query

        if 'date_min' in args:
            date_start = datetime.strptime(args["date_min"], '%Y-%m-%d')
            print(date_start)
            query = query.filter(Cours.end_time >= date_start)

        if 'date_max' in args:
            date_end = datetime.strptime(args["date_max"], '%Y-%m-%d') + timedelta(days=1)
            print(date_end)
            query = query.filter(Cours.start_time < date_end)

        if type(publish) == bool:
            query = query.filter(Cours.is_published == publish)

        if 'room' in args:
            query = query.filter(Cours.name_salle == args["room"])
        if 'teacher' in args:
            query = query.filter(Cours.id_enseignant == args["teacher"])
        if 'group' in args:
            query = query.filter(Cours.id_group == args["group"])
        if 'resource' in args:
            query = query.filter(Cours.initial_ressource == args["resource"])

        return query.all()
    
    @staticmethod
    def delete_course(id):
        course = Cours.query.get(id)
        db.session.delete(course)
        db.session.commit()
        return course
    
    @staticmethod
    def update_course(id, start_time, end_time, initial_ressource, id_group, name_salle = None,id_enseignant= None, **kwargs):
        course = Cours.query.get(id)

        course.start_time = start_time
        course.end_time = end_time
        course.id_enseignant = id_enseignant if id_enseignant else db.null()
        course.initial_ressource = initial_ressource
        course.id_group = id_group
        course.name_salle = name_salle if name_salle else db.null()
        
        db.session.commit()
        return course
    

    @staticmethod
    def can_create_course(start_time, end_time, id_group, name_salle = None, id_enseignant = None,   **kwargs):

        if type(start_time) != str:
            start_time = start_time.strftime("%Y-%m-%d %H:%M:%S")
        if type(end_time) != str:
            end_time = end_time.strftime("%Y-%m-%d %H:%M:%S")

        if start_time >= end_time:
            return {"response" : "start_time doit être inférieur à end_time"}, 400

        try:
            group_depends = GroupeService.get_tree(id_group)
        except Exception as e:
            return {"response" : "Groupe introuvable"}, 404

        for group in group_depends:
            current_group = GroupeService.get_groupe_by_id(group)
            #Si un cours est déjà prévu entre start_time et end_time
            courses = Cours.query.filter_by(id_group=group).filter(and_(Cours.start_time > start_time, Cours.start_time < end_time)).all()
            if len(courses) > 0: return {"error" :f"Le groupe {current_group.name} à déjà cours !"}, 409
            courses = Cours.query.filter_by(id_group=group).filter(and_(Cours.end_time > start_time, Cours.end_time < end_time)).all()
            if len(courses) > 0: return {"error" :f"Le groupe {current_group.name} à déjà cours !"}, 409

            courses = Cours.query.filter_by(id_group=group).filter(and_(Cours.start_time == start_time, Cours.end_time == end_time)).all()
            if len(courses) > 0: return {"error" :f"Le groupe {current_group.name} à déjà cours !"}, 409

            #Si une salle est déjà prise entre start_time et end_time
            if name_salle:
                courses = Cours.query.filter_by(name_salle=name_salle).filter(Cours.start_time > start_time).filter(Cours.start_time < end_time).all()
                if len(courses) > 0: return {"error" :"Cette salle est déjà prise"},409

                courses = Cours.query.filter_by(name_salle=name_salle).filter(Cours.end_time > start_time).filter(Cours.end_time < end_time).all()
                if len(courses) > 0: return {"error" :"Cette salle est déjà prise"},409


            if id_enseignant:
                courses = Cours.query.filter_by(id_enseignant=id_enseignant).filter(Cours.start_time > start_time).filter(Cours.start_time < end_time).all()
                if len(courses) > 0: return {"warning" :"Attention ! Ce professeur à déjà un cours dans cette plage horaire"},201

                courses = Cours.query.filter_by(id_enseignant=id_enseignant).filter(Cours.end_time > start_time).filter(Cours.end_time < end_time).all()
                if len(courses) > 0: return {"warning" :"Attention ! Ce professeur à déjà un cours dans cette plage horaire"},201


        return None, 200
    
    @staticmethod
    def publish():
        courses = Cours.query.filter_by(is_published=False).all()
        for course in courses:
            course.is_published = True
        db.session.commit()
        return courses
    
    @staticmethod
    def cancel():
        courses = Cours.query.filter_by(is_published=False).all()
        for course in courses:
            db.session.delete(course)
        db.session.commit()
        return courses
    
    
    


    

