from models.ResponsableEdt import ResponsableEdt
from database.config import db 
from services.ResponsableEdtService import ResponsableEdtService


dataRespEDT = [

  {
      'name' : 'Philippe',
      'lastname' : 'Bonnot',
      'identifier' : 'philippe_bonnot1',
      'password' : 'philippe1234'
  },

  {
      'name' : 'Sandrine',
      'lastname' : 'Bonjour',
      'identifier' : 'sandrine_bonjour',
      'password' : 'sandrine1234'
  }
]


for resp in dataRespEDT:
    ResponsableEdtService.create_responsable_edt(resp)


    