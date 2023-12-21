import pytest
from flask import Flask
from models.Salle import Salle
from flask_sqlalchemy import SQLAlchemy
from services.SalleService import SalleService
from database.config import db

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

def test_create_salle(app):
    with app.app_context():
        # Create a test instance
        salle_data = {
            'name': 'A2-05',
            'ordi': 25,
            'tableauNumerique': 1,
            'videoProj': 1
        }

        # Use SalleService.create_salle with the provided data
        salle = SalleService.create_salle(**salle_data)

        # Retrieve the instance from the database
        retrieved_salle = SalleService.get_salle_by_name('A2-05')

        # Perform assertions to check if the instance was added and retrieved correctly
        assert retrieved_salle is not None
        assert retrieved_salle.ordi == 25
        assert retrieved_salle.tableauNumerique == 1
        assert retrieved_salle.videoProjecteur == 1

        # Clean up the database (optional)
        db.session.delete(retrieved_salle)
        db.session.commit()
