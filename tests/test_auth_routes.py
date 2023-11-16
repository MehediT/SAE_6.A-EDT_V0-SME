import json
from flask import Flask, request, jsonify
import pytest
from flask import UserService
from unittest.mock import patch


def test_register(client):
    # Données de test pour l'utilisateur
    user_data = {
        'identifier': 'test_user',
        'password': 'password123',
        'role': 'user',
        'name': 'John',
        'lastname': 'Doe'
    }

    
    response = client.post('/user', json=user_data)

    # réponse correcte (code 200)
    assert response.status_code == 200

    assert 'Nouvel utilisateur ajouté avec succès' in response.json['message']



def test_register_missing_data(client):
    
    # Données de test pour l'utilisateur
    user_data = {
        'password': 'password123',
        'role': 'user',
        'name': 'John',
        'lastname': 'Doe'
    }

    
    response = client.post('/user', json=user_data)

    # réponse fausse (code 400)
    assert response.status_code == 400

    assert 'error' in response.json
    


def test_login(client):
    # Données de test pour la requête POST de login
    login_data = {
        'identifier': 'test_user',
        'password': 'password123',
    }

    MockUser = {'identifier':'test_user','password':'password123'}
    
    # Mock get_by_identifier   
    with patch.object(UserService, 'get_by_identifier', return_value=MockUser('identifier', 'password')) as mock_get_user:
        # Mock checkPassword
        with patch.object(MockUser, 'check_password', return_value=True) as mock_check_password:
            with client() as client:
                response = client.post('/login', json=login_data)

            # réponse réussie (code 200)
            assert response.status_code == 200
