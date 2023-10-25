from flask import Flask
from .auth_routes import auth_bp
from .api_routes import api_bp

def register_routes(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(api_bp)

# Exportez la fonction pour l'utiliser dans app.py