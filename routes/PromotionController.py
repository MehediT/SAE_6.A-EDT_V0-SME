from flask import Blueprint, jsonify, request
from services.PromotionService import PromotionService

promotion_bp = Blueprint('promotion', __name__)

@promotion_bp.route('/promotions', methods=['GET'])
def get_all_promotions():

    try:
        # Récupérer toutes les abscences d'un étudiant
        promotions = PromotionService.get_all_promos()   

        promotions_dict = [promotion.to_dict() for promotion in promotions]
        return jsonify(promotions_dict),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    
@promotion_bp.route('/promotion/<id>', methods=['GET'])
def get_promotion_by_id(id):

    try:
        # Récupérer toutes les abscences d'un étudiant
        promotion = PromotionService.get_promo_by_id(id)   

        if not promotion:
            return jsonify({'error': 'Promotion not found'}),404

        return jsonify(promotion.to_dict()),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    
@promotion_bp.route('/promotion', methods=['POST'])
def create_promotion():
    try:
        data = request.json
        promotion = PromotionService.create_promo(data)
        return jsonify(promotion.to_dict()),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    
@promotion_bp.route('/promotion/<id>', methods=['DELETE'])
def delete_promotion(id):
    try:
        promotion = PromotionService.delete_promo(id)
        if not promotion:
            return jsonify({'error': 'Promotion not found'}),404
        
        return jsonify(promotion.to_dict()),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    

@promotion_bp.route('/promotion/<id>', methods=['PUT'])
def update_promotion(id):
    try:
        data = request.json
        if 'id' in data:
            del data['id']

        promotion = PromotionService.update_promo(id=id, **data)
        if not promotion:
            return jsonify({'error': 'Promotion not found'}),404
        
        return jsonify(promotion.to_dict()),200
    except Exception as e:
        return jsonify({'error': str(e)}),403