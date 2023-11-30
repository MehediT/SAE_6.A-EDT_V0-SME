from flask import Blueprint, jsonify, send_from_directory, request
from services.UserService import UserService
from models.User import User
from models.Absence import Absence
from functools import wraps
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity)
from models.RespEDTPromo import RespEDTPromo
from services.RespEDTPromoService import RespEDTPromoService

respEdtPromo_bp = Blueprint('respEDTPromo', __name__)



@respEdtPromo_bp.route('/respEdtPromo/create', methods=['POST'])
def create_respedt_promo():
    
    idRespEdt = request.json.get('idRespEDT')
    promoName = request.json.get('promoName')

    try:
        # Création d'un responsable EDT
        RespEDTPromoService.create_respedt_promo(idRespEdt,promoName)
        return jsonify({'message': 'Nouvel responsable EDT crée avec succès'}),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    


    

@respEdtPromo_bp.route('/respEdtPromo/getPromoByRespedt', methods=['GET'])
def get_promo_by_respedt():
    
    idRespEdt = request.json.get('idRespEDT')

    try:
        # Récupérer une promotion affilié à son responsable EDT
        RespEDTPromoService.get_promo_by_respedt(idRespEdt)
        return jsonify({'message': 'Imformations sur la promotion envoyés avec succès'}),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    


@respEdtPromo_bp.route('/respEdtPromo/getRespedtByPromo', methods=['GET'])
def get_respedt_by_promo():
    
    promoName = request.json.get('promoName')

    try:
        # Récupérer un responsable EDT avec la promotion
        RespEDTPromoService.get_respedt_by_edt(promoName)
        return jsonify({'message': 'Imformations sur le responsable EDT envoyés avec succès'}),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
    


@respEdtPromo_bp.route('/respEdtPromo/delete', methods=['DELETE'])
def delete_respedt_promo():
    
    idRespEdt = request.json.get('idRespEDT')
    promoName = request.json.get('promoName')

    try:
        # Suppression d'un responsable EDT
        RespEDTPromoService.delete_respedtpromo(idRespEdt,promoName)
        return jsonify({'message': 'Responsable EDT supprimer avec succès'}),200
    except Exception as e:
        # En cas d'erreur, annulez la transaction et renvoyez un message d'erreur
        # db.session.rollback()
        return jsonify({'error': str(e)}),403
