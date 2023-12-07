from database.config import db
from models.relations.user_groupe import student_course_association

class UserGroupeService:

  @staticmethod
  def create_user_groupe(idStudent,idGroupe):
    user_groupe = student_course_association().append(idStudent,idGroupe) 

    db.session.add(user_groupe)
    db.session.commit()

  @staticmethod
  def get_groupe_etudiant(idStudent,idGroupe):
    return student_course_association.query.filter_by(idStudent=idStudent).filter_by(idGroupe=idGroupe).first()
  
  @staticmethod
  def get_etudiant_by_groupe(idGroupe, idStudent):
    return student_course_association.query.filter_by(idGroupe=idGroupe).filter_by(idStudent=idStudent).all()
  
  @staticmethod
  def set_groupe_etudiant(idStudent, newIdGroupe):
    etudiant_groupe_to_modify = student_course_association.query.filter_by(idStudent=idStudent).first()

    etudiant_groupe_to_modify.idGroupe = newIdGroupe
    db.session.commit()

  @staticmethod
  def delete_user_groupe(idStudent):
    user_groupe_delete = student_course_association.query.filter_by(idStudent=idStudent).first()

    db.session.delete(user_groupe_delete)
    db.session.commit()  
