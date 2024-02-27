from models.relations.affiliation_resp_edt import affiliation_resp_edt
from database.config import db 
from services.AffiliationRespEdtService import AffiliationRespEdtService


dataAffiliationRespEdt = []


for respEdt in dataAffiliationRespEdt:

    idResp = respEdt["id_resp"]
    id_promo = respEdt["id_promo"]
    AffiliationRespEdtService.affiliate_respedt_to_promo(idResp,id_promo)

    

