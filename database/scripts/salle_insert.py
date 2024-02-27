from models.Salle import Salle
from database.config import db 
from services.SalleService import SalleService



dataSalles = []


for salles in dataSalles:



    SalleService.create_salle(salles)

    