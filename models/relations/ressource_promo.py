from database.config import db

affiliation_ressource_promo = db.Table(
    'affiliation_ressource_promo',
    db.Column('id_ressource', db.String(5), db.ForeignKey('ressources.initial')),
    db.Column('id_promo', db.Integer, db.ForeignKey('promotion.id_promo'))
)