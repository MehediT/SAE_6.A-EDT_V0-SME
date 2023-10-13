from flask import Flask, request, jsonify
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import bcrypt
from flask_migrate import Migrate




#Import personnalisé
#import model


load_dotenv()

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'votre_clé_secrète'  # Remplacez 'votre_clé_secrète' par une clé secrète forte et sécurisée
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

db = SQLAlchemy(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)


@app.route('/user', methods=['POST'])
def register():
    identifier = request.json.get('identifier')
    password = request.json.get('password')
    role = request.json.get('role')
    name = request.json.get('name')
    lastname = request.json.get('lastname')

    try:
        # Créez un nouvel utilisateur
        new_user = User(identifier=identifier, password=password, role=role, name=name, lastname=lastname)
        
        # Ajoutez le nouvel utilisateur à la session et commettez les changements
        db.session.add(new_user)
        db.session.commit()

        # La transaction a réussi, renvoyez une réponse de succès
        return jsonify({'message': 'Nouvel utilisateur ajouté avec succès'})
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        db.session.rollback()
        return jsonify({'error': str(e)})

@app.route('/login', methods=['POST'])
def login():
    identifier = request.json.get('identifier')
    password = request.json.get('password')

    user = get_user_by_identifier(identifier)
    if (user is not None):
        # Vérifiez le nom d'utilisateur et le mot de passe (par exemple, dans une base de données)
        # Si la vérification est réussie, générez un jeton d'accès JWT
        if (user.check_password(password)):
            access_token = create_access_token(identity=identifier)
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
    identifier = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(64), nullable=False)
    name = db.Column(db.String(64), nullable=False)
    lastname = db.Column(db.String(64), nullable=False)


    def __init__(self, identifier, password, role, name, lastname):
        self.identifier = identifier
        self.role = role
        self.name = name
        self.lastname = lastname


        self.set_password(password)  # Utilisez la méthode pour définir le mot de passe
        
    def set_password(self, password):
        # Utilisez hashlib pour hacher le mot de passe en MD5
        salt = bcrypt.gensalt()
        self.password = bcrypt.hashpw(password.encode('utf-8'), salt)
    def check_password(self, password):
        # Vérifiez si le mot de passe fourni correspond au hachage dans la base de données
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

def get_user_by_identifier(identifier):
    user = User.query.filter_by(identifier=identifier).first()
    return user


with app.app_context():
    db.create_all()
    
if __name__ == '__main__':
    app.run(debug=True)