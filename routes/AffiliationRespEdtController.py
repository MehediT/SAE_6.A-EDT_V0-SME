from flask import Blueprint, jsonify, request
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity)
from services.AffiliationRespEdtService import AffiliationRespEdtService

affiliationrespedt_bp = Blueprint('affiliationrespedt', __name__)



@affiliationrespedt_bp.route('/affiliateRespEdt', methods=['POST'])
@jwt_required()
def affiliate_respedt_to_promo():

    idResp = request.json["id_resp"]
    idPromo = request.json["id_promo"]
    
    try:
        # Associer un respEdt à une promo
        affiliate_respEdt = AffiliationRespEdtService.affiliate_respedt_to_promo(idResp,idPromo)

        return jsonify(affiliate_respEdt.to_dict()),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403


@affiliationrespedt_bp.route('/affiliateRespEdt/getPromosByResp/<idResp>', methods=['GET'])
@jwt_required()
def get_promos_for_respedt(idResp):

    try:
        # Associer un respEdt à une promo
        affiliate_respEdt = AffiliationRespEdtService.get_promos_for_respedt(idResp)

        if not affiliate_respEdt:
            return jsonify({'error': 'Promotions not found'}),201

        return jsonify(affiliate_respEdt),200
    except Exception as e:
        return jsonify({'error': str(e)}),403



@affiliationrespedt_bp.route('/affiliateRespEdt/delete/<idResp>', methods=['DELETE'])
@jwt_required()
def delete_affiliate_respedt_to_promo(idResp):
    
    try:
        # Associer un respEdt à une promo
        affiliate_respEdt = AffiliationRespEdtService.delete_respEdt_promo(idResp)

        return jsonify({"message": "RespEdtPromo supprimé du groupe avec succès"}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 403

