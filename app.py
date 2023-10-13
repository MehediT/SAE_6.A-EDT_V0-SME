from flask import Flask, request
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import bcrypt



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
    identifiant = request.json.get('identifiant')
    password = request.json.get('password')

    user = get_user_by_identifiant(identifiant)
    if (user is not None):
        # Vérifiez le nom d'utilisateur et le mot de passe (par exemple, dans une base de données)
        # Si la vérification est réussie, générez un jeton d'accès JWT
        if (user.check_password(password)):
            access_token = create_access_token(identity=identifiant)
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
    identifiant = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)

    def __init__(self, identifiant, password):
        self.identifiant = identifiant
        self.set_password(password)  # Utilisez la méthode pour définir le mot de passe
        
    def set_password(self, password):
        # Utilisez hashlib pour hacher le mot de passe en MD5
        salt = bcrypt.gensalt()
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)
    def check_password(self, password):
        # Vérifiez si le mot de passe fourni correspond au hachage dans la base de données
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

def get_user_by_identifiant(identifiant):
    user = User.query.filter_by(identifiant=identifiant).first()
    return user

with app.app_context():
    db.create_all()
    # new_user = User(identifiant='nom_utilisateur', password='mot_de_passe')
    # db.session.add(new_user)
    # db.session.commit()
    
if __name__ == '__main__':
    app.run(debug=True)