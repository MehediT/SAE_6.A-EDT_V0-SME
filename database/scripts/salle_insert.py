from models.Salle import Salle
from database.config import db 
from services.SalleService import SalleService



dataSalles = [
    {
        'name': 'B1-09',
        'ordi' : 30,
        'tableauNumerique' : 1,
        'videoProjecteur' : 1
    },
    {
        'name': 'B1-10',
        'ordi' : 30,
        'tableauNumerique' : 1,
        'videoProjecteur' : 1
    },
    {
        'name': 'B1-11',
        'ordi' : 30,
        'tableauNumerique' : 1,
        'videoProjecteur' : 1
    },
    {
        'name': 'B1-12',
        'ordi' : 30,
        'tableauNumerique' : 1,
        'videoProjecteur' : 1
    },
    {
        'name': 'B1-13',
        'ordi' : 30,
        'tableauNumerique' : 1,
        'videoProjecteur' : 1
    },
    {
        'name': 'B1-14',
        'ordi' : 30,
        'tableauNumerique' : 1,
        'videoProjecteur' : 1
    },
    {
        'name': 'B1-15',
        'ordi' : 30,
        'tableauNumerique' : 1,
        'videoProjecteur' : 1
    },
    {
        'name': 'B1-16',
        'ordi' : 30,
        'tableauNumerique' : 1,
        'videoProjecteur' : 1
    },
    {
        'name': 'B1-17',
        'ordi' : 30,
        'tableauNumerique' : 1,
        'videoProjecteur' : 1
    },
    {
        'name': 'B1-18',
        'ordi' : 30,
        'tableauNumerique' : 1,
        'videoProjecteur' : 1
    },
]


for salles in dataSalles:



    SalleService.create_salle(salles)

    