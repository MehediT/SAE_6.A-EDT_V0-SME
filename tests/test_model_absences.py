from models.Absence import Absence
from models.Cours import Cours
from models.User import User
import pytest
from database.config import db

def test_absence_initialization(app):
    # Test the initialization of the Absence class

    # Create test instances for related models
    user = User(username="test_user")
    cours = Cours(id=1, name="Test Course")

    # Add the instances to the test database
    with app.app_context():
        db.session.add(user)
        db.session.add(cours)
        db.session.commit()

    # Create a test instance of Absence
    absence = Absence(idEtudiant="test_user", idCour=1)

    # Add the Absence instance to the test database
    with app.app_context():
        db.session.add(absence)
        db.session.commit()

    # Retrieve the Absence instance from the database
    with app.app_context():
        retrieved_absence = Absence.query.filter_by(idEtudiant="test_user", idCour=1).first()

    # Perform assertions to check if the Absence instance was added and retrieved correctly
    assert retrieved_absence is not None
    assert retrieved_absence.idEtudiant == "test_user"
    assert retrieved_absence.idCour == 1
    assert retrieved_absence.justifiée is False

    with app.app_context():
        db.session.delete(retrieved_absence)
        db.session.delete(user)
        db.session.delete(cours)
        db.session.commit()