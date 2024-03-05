from models.Ressources import Ressources
from database.config import db 
from services.RessourcesService import RessourcesService


dataRessources = [
    {
      "initial": "R3-01",
      "name": "Modélisation",
      "id_promo": 1,
      "color": "#0D4378"
    },
    {
      "initial": "R3-02",
      "name": "Dev Mobile",
      "id_promo": 1,
      "color": "#0D4378"
    },
    {
      "initial": "R3-03",
      "name": "Data Science",
      "id_promo": 1,
      "color": "#0D4378"
    },
    {
      "initial": "R3-04",
      "name": "IA",
      "id_promo": 1,
      "color": "#0D4378"
    },
    {
      "initial": "R3-05",
      "name": "Cybersécurité",
      "id_promo": 1,
      "color": "#0D4378"
    },
    {
      "initial": "R3-06",
      "name": "Web Développement",
      "id_promo": 1,
      "color": "#0D4378"
    },
    {
      "initial": "R3-07",
      "name": "Réseaux",
      "id_promo": 1,
      "color": "#0D4378"
    },
    {
      "initial": "R3-08",
      "name": "Cloud Computing",
      "id_promo": 1,
      "color": "#0D4378"
    },
    {
      "initial": "R3-09",
      "name": "Big Data",
      "id_promo": 1,
      "color": "#0D4378"
    },
    {
      "initial": "R3-10",
      "name": "Blockchain",
      "id_promo": 1,
      "color": "#0D4378"
    }
]


for ressource in dataRessources:
    RessourcesService.create_resource(ressource)