from models.Absence import Absence
from models.Cours import Cours
from models.User import User
import pytest
from database.config import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from tests.conftests import create_app, app

def create_app():
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  db.init_app(app)

  return app



@pytest.fixture(name="app")
def app():
    app = create_app()

    with app.app_context():
        db.create_all()

    yield app

    with app.app_context():
        db.drop_all()

def test_absence_initialization(app):
    # Test the initialization of the Absence class

    # Create test instances for related models
    user = User(username="jonas_obrun",password="jonas1234",role="ROLE_STUDENT",name="Jonas",lastname="Obrun")
    cours = Cours(start_time="2023-12-02 23:55:00",end_time="2023-12-03 01:00:00",initial_ressource="R5A05",id_group= 2)


    # Add the instances to the test database
    with app.app_context():
        db.session.add(user)
        db.session.add(cours)
        db.session.commit()

    # Create a test instance of Absence
    absence = Absence(idEtudiant="jonas_obrun", idCour=1)

    # Add the Absence instance to the test database
    with app.app_context():
        db.session.add(absence)
        db.session.commit()

    # Retrieve the Absence instance from the database
    with app.app_context():
        retrieved_absence = Absence.query.filter_by(idEtudiant="jonas_obrun", idCour=1).first()

    # Perform assertions to check if the Absence instance was added and retrieved correctly
    assert retrieved_absence is not None
    assert retrieved_absence.idEtudiant == "jonas_obrun"
    assert retrieved_absence.idCour == 1
    assert retrieved_absence.justifiée is False

    with app.app_context():
        db.session.delete(retrieved_absence)
        db.session.delete(user)
        db.session.delete(cours)
        db.session.commit()