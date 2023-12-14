import pytest
from database.config import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models.User import User
import bcrypt

def check_password(self, password):
    # Check if the provided password matches the hashed password
    return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)


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


def test_user_initialization(app):
    # Test the initialization of the User class

    # Create a test instance
    user = User(
        username="jonas_obrun",
        password="jonas1234",
        role="ROLE_STUDENT",
        name="jonas",
        lastname="obrun"
    )

    # Add the instance to the test database
    with app.app_context():
        db.session.add(user)
        db.session.commit()

    # Retrieve the instance from the database
    with app.app_context():
        retrieved_user = User.query.filter_by(username="jonas_obrun").first()

    # Perform assertions to check if the instance was added and retrieved correctly
    assert retrieved_user is not None
    assert retrieved_user.password.check_password("jonas1234")
    assert retrieved_user.role == "ROLE_STUDENT"
    assert retrieved_user.name == "jonas"
    assert retrieved_user.lastname == "obrun"

    # Clean up the database (optional)
    with app.app_context():
        db.session.delete(retrieved_user)
        db.session.commit()