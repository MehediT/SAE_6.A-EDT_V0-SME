from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

# Configuration de la base de données
DB_URI = os.environ.get('DATABASE_URL')

def configure_database(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)