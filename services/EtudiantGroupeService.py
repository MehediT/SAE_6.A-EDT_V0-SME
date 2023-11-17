from database.config import db
from models.EtudiantGroupe import EtudiantGroupe

class EtudiantGroupeService:

  @staticmethod
  def create_etudiant_groupe(idEtudiant, idGroupe):
    etudiant_groupe = EtudiantGroupe(idEtudiant=idEtudiant, idGroupe=idGroupe)

    db.session.add(etudiant_groupe)
    db.session.commit()

  @staticmethod
  def get_groupe_etudiant(idEtudiant, promo):
    return EtudiantGroupe.query.filter_by(idEtudiant=idEtudiant).filter_by(promotion=promo).first().idGroupe
  
  @staticmethod
  def get_etudiant_by_groupe(idGroupe, idPromo):
    return EtudiantGroupe.query(EtudiantGroupe.idEtudiant).filter_by(idGroupe=idGroupe).filter_by(idGroupe=idGroupe).all()
  
  @staticmethod
  def set_groupe_etudiant(idEtudiant, newIdGroupe, newPromo):
    etudiant_groupe_to_modify = EtudiantGroupe.query.filter_by(idEtudiant=idEtudiant).first()

    etudiant_groupe_to_modify.idGroupe = newIdGroupe
    etudiant_groupe_to_modify.promotion = newPromo

    db.session.commit()

  @staticmethod
  def delete_etudiant_groupe(idEtudiant):
    etudiant_to_delete = EtudiantGroupe.query.filter_by(idEtudiant=idEtudiant).first()

    db.session.delete(etudiant_to_delete)
    db.session.commit()  
