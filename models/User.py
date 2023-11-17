from database.config import db
from datetime import datetime
import bcrypt


class User(db.Model):
    __tablename__= "user"

    id = db.Column(db.Integer, primary_key=True)
    identifier = db.Column(db.String(80), unique=True, nullable=False)
    absence = db.relationship('Absence', backref='idUser', lazy='dynamic')
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(64), nullable=False)
    name = db.Column(db.String(64), nullable=False)
    lastname = db.Column(db.String(64), nullable=False)
    
    enseignant = db.relationship('Enseignant', backref='user', lazy=True)
    etudiantGroupe = db.relationship('EtudiantGroupe', backref='etudiant_appartient_groupe', lazy='dynamic')
    managed_promo_respEdt = db.relationship('RespEDTPromo', backref='what_access_respEdt', lazy='dynamic')




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

    def to_dict(self):
        return {
            'id': self.id,
            'identifier': self.identifier,
            'role': self.role,
            'name': self.name,
            'lastname': self.lastname
        }