from flask import Flask, request
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy



#Import personnalisé
#import model


load_dotenv()

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'votre_clé_secrète'  # Remplacez 'votre_clé_secrète' par une clé secrète forte et sécurisée
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

db = SQLAlchemy(app)
jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    # Vérifiez le nom d'utilisateur et le mot de passe (par exemple, dans une base de données)
    # Si la vérification est réussie, générez un jeton d'accès JWT
    if username == 'utilisateur' and password == 'motdepasse':
        access_token = create_access_token(identity=username)
        return {'access_token': access_token}, 200
    else:
        return {'message': 'Authentification échouée'}, 401
    
@app.route('/test', methods=['GET'])
@jwt_required()
def ressource_protégée():
    current_user = get_jwt_identity()
    return {'message': 'Ceci est une ressource protégée', 'user': current_user}



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

with app.app_context():
    db.create_all()
    
if __name__ == '__main__':
    app.run(debug=True)