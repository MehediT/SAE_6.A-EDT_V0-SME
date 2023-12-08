from flask import Blueprint, jsonify, request
from services.AffiliationRespEdtService import AffiliationRespEdtService

affiliationrespedt_bp = Blueprint('affiliationrespedt', __name__)



@affiliationrespedt_bp.route('/affiliateRespEdt', methods=['POST'])
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


@affiliationrespedt_bp.route('/affiliateRespEdt/getRespEdtByPromo/<idPromo>/<idResp>', methods=['GET'])
def get_respedt_by_promo(idPromo,idResp):
    
    try:
        # Récuperer un RespEdt à partir d'une promo
        affiliate_respEdt = AffiliationRespEdtService.get_respedt_by_promo(idPromo,idResp)

        return jsonify(affiliate_respEdt.to_dict()),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403



@affiliationrespedt_bp.route('/affiliateRespEdt/getPromoByRespEdt/<idResp>/<idPromo>', methods=['GET'])
def get_respedt_by_promo(idPromo,idResp):
    
    try:
        # Récuperer une promo à partir d'un RespEdt
        affiliate_respEdt = AffiliationRespEdtService.get_promo_by_respedt(idPromo,idResp)

        return jsonify(affiliate_respEdt.to_dict()),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403


@affiliationrespedt_bp.route('/affiliateRespEdt/delete/<idResp>', methods=['DELETE'])
def affiliate_respedt_to_promo(idResp):
    
    try:
        # Associer un respEdt à une promo
        affiliate_respEdt = AffiliationRespEdtService.delete_respEdt_promo(idResp)

        if not affiliate_respEdt:
            return jsonify({'error': 'Responsable EDT not found'}),403

        return jsonify(affiliate_respEdt.to_dict()),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403

