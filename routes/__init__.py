from flask import Flask
from .auth_routes import auth_bp
from .api_routes import api_bp
from .cours_routes import cours_bp
from .UserController import user_bp
from .TeacherController import teacher_bp

def register_routes(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(cours_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(teacher_bp)

# Exportez la fonction pour l'utiliser dans app.py