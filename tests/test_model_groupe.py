import pytest
from flask import Flask
from database.config import db
from models.Groupe import Groupe
import warnings

# Suppress SQLAlchemy Legacy API Warning
warnings.filterwarnings("ignore", category=DeprecationWarning, module="sqlalchemy.orm.query.*")

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

def test_create_groupe(app):
    with app.app_context():
        # Create a test groupe
        groupe_data = {'name': 'Test Groupe', 'id_group_parent': None}
        groupe = Groupe(**groupe_data)

        # Commit the groupe to the database
        db.session.add(groupe)
        db.session.commit()

        # Check if the groupe was created
        assert groupe.id is not None
        assert groupe.name == 'Test Groupe'
        assert groupe.id_group_parent is None


def test_create_groupe_with_parent(app):
    with app.app_context():
        # Create a parent groupe
        parent_data = {'name': 'Parent Groupe', 'id_group_parent': None}
        parent = Groupe(**parent_data)

        # Commit the parent to the database
        db.session.add(parent)
        db.session.commit()

        # Create a child groupe with the parent
        child_data = {'name': 'Child Groupe', 'id_group_parent': parent.id}
        child = Groupe(**child_data)

        # Commit the child to the database
        db.session.add(child)
        db.session.commit()

        # Check if both groupes were created
        assert parent.id is not None
        assert child.id is not None
        assert child.id_group_parent == parent.id


def test_create_groupe_with_nonexistent_parent(app):
    with app.app_context():
        # Attempt to create a groupe with a nonexistent parent
        groupe_data = {'name': 'Test Groupe', 'id_group_parent': 999}
        with pytest.raises(Exception, match="Groupe parent does not exist"):
            groupe = Groupe(**groupe_data)
            db.session.add(groupe)
            db.session.commit()


def test_to_dict_method(app):
    with app.app_context():
        # Create a test groupe
        groupe_data = {'name': 'Test Groupe', 'id_group_parent': None}
        groupe = Groupe(**groupe_data)

        # Commit the groupe to the database
        db.session.add(groupe)
        db.session.commit()

        # Convert the groupe to a dictionary
        groupe_dict = groupe.to_dict()

        # Check if the dictionary has the expected keys and values
        assert groupe_dict['id'] == groupe.id
        assert groupe_dict['name'] == groupe.name
        assert groupe_dict['id_group_parent'] == groupe.id_group_parent

