from sqlalchemy import update
from models.Groupe import Groupe
from models.User import User
from models.Student import Student
from services.GroupeService import GroupeService
from database.config import db
from models.relations.user_groupe import student_course_association
from sqlalchemy.orm import joinedload
from sqlalchemy.orm import aliased
import random


class UserGroupeService:

    @staticmethod
    def add_user_to_group(user_id, group_id):
        # Create an instance of the user_groupe table
        user_group_association = student_course_association.insert().values(id_student=user_id, id_group=group_id)

        # Add the association to the database session
        db.session.execute(user_group_association)

        # Commit the changes to the database
        db.session.commit()

    @staticmethod
    def get_groupe_etudiant(idStudent,idGroupe):
        return student_course_association.query.filter_by(idStudent=idStudent).filter_by(idGroupe=idGroupe).first()

    @staticmethod
    def get_groupes_for_student(idStudent):
        query = db.session.query(student_course_association).filter_by(id_student=idStudent)

        result = query.all()
        groupes = [id_group for id_student, id_group in result]

        return groupes

    @staticmethod
    def get_etudiant_by_groupe(idGroupe, idStudent):
        return student_course_association.query.filter_by(idGroupe=idGroupe).filter_by(idStudent=idStudent).all()

    @staticmethod
    def update_student_group(student_id, new_group_id, old_group_id):
        try:
            db.session.execute(
                student_course_association.update().where(
                    (student_course_association.c.id_student == student_id) &
                    (student_course_association.c.id_group == old_group_id)
                ).values(id_group=new_group_id)
            )
            db.session.commit()
            return {"message": "Groupe d'étudiants mis à jour avec succès"}
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}


    # @staticmethod
    # def delete_user_groupe(idStudent):
    #   try:
    #       # Utilisez delete() directement sur la table d'association
    #       table = Student.query.join(student_course_association).join(Groupe).filter((student_course_association.c.id_student == Student.id_student) & (student_course_association.c.id_group == Groupe.id)).all()
    #       table.query.filter_by(id_student=idStudent).delete()
    #       db.session.commit()
    #   except Exception as e:
    #       db.session.rollback()
    #       raise e

    @staticmethod
    def delete_user_groupe(idStudent):
        try:
            # Use delete() directly on the association table
            db.session.query(student_course_association).filter(
                (student_course_association.c.id_student == idStudent) &
                (student_course_association.c.id_group == Groupe.id)
            ).delete(synchronize_session=False)

            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e




    # @staticmethod
    # def get_etudiants_for_groupe(idGroupe):
    #   query = db.session.query(Student.name, Student.lastname).join(student_course_association).filter(student_course_association.c.id_group == idGroupe)
    #   result = query.all()

    #   etudiants_list = [{"name": name, "lastname": lastname} for name, lastname in result]

    #   return etudiants_list

    @staticmethod
    def get_etudiants_for_groupe(idGroupe):
        query = db.session.query(
            student_course_association.c.id_group,
            Student.id_student,
            Student.name,
            Student.lastname
        ).join(Student).filter(student_course_association.c.id_group == idGroupe)

        result = query.all()

        etudiants_list = [{"id_group": id_group, "id_student": id_student, "name": name, "lastname": lastname} for id_group, id_student, name, lastname in result]

        return etudiants_list

    # @staticmethod
    # def modifier_etudiant_groupe(idStudent, idGroupe):
    #   user_groupe_to_modify = student_course_association.query.filter_by(idStudent=idStudent).first()

    #   user_groupe_to_modify.idGroupe = idGroupe
    #   db.session.commit()

    @staticmethod
    def update_promo_etudiants(idEtudiants, idNvPromo):
        all_groups_of_new_promo = GroupeService.get_tree(idNvPromo)
        group_tp_new_promo = []
        students_to_add = idEtudiants.copy()
        
        for group in all_groups_of_new_promo:
            group_has_children = GroupeService.get_children(group)
            
        if len(group_has_children.get('children'))==0 :
            group_tp_new_promo.append(group)

        else:
            print(f"Warning: get_children returned None for group {group}")
        
        print("group_tp_new_promo",group_tp_new_promo)
        students_per_group = []
        
        if len(group_tp_new_promo) > 0:
            nb_students_per_group = len(idEtudiants) // len(group_tp_new_promo)
            
            print("nb_students_per_group",nb_students_per_group)
            for group in group_tp_new_promo:
                group_students = random.sample(students_to_add, min(nb_students_per_group, len(students_to_add)))

                print("group_students",group_students)
                for student in group_students:
                    print("students_to_add",students_to_add)
                    students_to_add.remove(student)
                    students_per_group.append([student, group])
                    print("students_per_group",students_per_group)
        else:
            print("No groups available in the new promotion.")
        
        return students_per_group        
    




        
        
    