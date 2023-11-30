from flask import Blueprint, jsonify, request
from services.RessourcesService import RessourcesService

ressource_bp = Blueprint('ressource', __name__)

@ressource_bp.route('/ressources', methods=['GET'])
def get_all_ressources():

    try:
        # Récupérer toutes les abscences d'un étudiant
        ressources = RessourcesService.get_all_ressources()   

        ressources_dict = [ressource.to_dict() for ressource in ressources]
        return jsonify(ressources_dict),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    
@ressource_bp.route('/ressource/<initial>', methods=['GET'])
def get_ressource(initial):
    try:
        # Récupérer toutes les abscences d'un étudiant
        ressource = RessourcesService.get_resource_by_initial(initial) 
        if not ressource:
            return jsonify({'error': 'Ressource not found'}),403  

        return jsonify(ressource.to_dict()),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    

@ressource_bp.route('/ressource', methods=['POST'])
def create_ressource():
    name = request.json.get('name')
    initial = request.json.get('initial')
    promo = request.json.get('promo')

    try:
        # Créer une salle
        ressource = RessourcesService.create_resource(name, initial, promo)

        return jsonify(ressource.to_dict()),200
    except Exception as e:

        return jsonify({'error': str(e)}),403
    
@ressource_bp.route('/ressource/<initial>', methods=['DELETE'])
def delete_ressource(initial):
    try: 
        ressource = RessourcesService.delete_ressource(initial)

        return jsonify(ressource.to_dict()),200
    except Exception as e:

        return jsonify({'error': str(e)}),403
    

@ressource_bp.route('/ressource/<initial>', methods=['PUT'])
def update_ressource(initial):
    name = request.json.get('name')
    promo = request.json.get('promo')

    try:
        ressource = RessourcesService.update_ressource(initial, name, promo)

        return jsonify(ressource.to_dict()),200
    except Exception as e:

        return jsonify({'error': str(e)}),403
    
    

# @ressource_bp.route('/salle/<name>', methods=['PUT'])
# def update_room(name):
#     ordi = request.json.get('ordi')
#     tableauNumerique = request.json.get('tableauNumerique')
#     videoProj = request.json.get('videoProjecteur')

#     try:
#         salle = SalleService.update_salle(name, ordi, tableauNumerique, videoProj)

#         return jsonify(salle.to_dict()),200
#     except Exception as e:
#         # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
#         # db.session.rollback()
#         return jsonify({'error': str(e)}),403