from flask import Blueprint, jsonify, request
from services.DisponibiliteService import DisponibiliteService

disponibilite_bp = Blueprint('disponibilite', __name__)


@disponibilite_bp.route('/disponibilite/<initial_enseignant>', methods=['GET'])
def get_enseignant_disponibilite(initial_enseignant):

    try:
        # Récupérer la disponibilité d'un enseignant
        dispo = DisponibiliteService.get_enseignant_disponibilite(initial_enseignant)   

        if not dispo:
            return jsonify({'error': 'Disponibilité non trouvé'}),404

        return jsonify(dispo.to_dict()),200
    
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    
from flask import Blueprint, jsonify, request
from services.DisponibiliteService import DisponibiliteService

disponibilite_bp = Blueprint('disponibilite', __name__)


@disponibilite_bp.route('/disponibilite', methods=['POST'])
def create_disponibilite():

    try:
        # Créer une disponibilité
        data = request.json
        dispo = DisponibiliteService.create_disponibilite(data)   

        return jsonify(dispo.to_dict()),200
    
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    

@disponibilite_bp.route('/disponibilite/delete/<id>', methods=['DELETE'])
def delete_disponibilite(id):
    
    try:
        # Supprimer une disponibilité
        dispo = DisponibiliteService.delete_disponibilite(id)  

        if not dispo:
            return jsonify({'error': 'Disponibilité non trouvé'}),404

        return jsonify(dispo.to_dict()),200
    
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403