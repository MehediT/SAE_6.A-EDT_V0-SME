from models.ResponsableEdt import ResponsableEdt
from database.config import db 
from services.ResponsableEdtService import ResponsableEdtService


dataRespEDT = [

  {
      'name' : 'Philippe',
      'lastname' : 'Bonnot',
      'username' : 'philippe_bonnot1',
      'password' : 'philippe1234'
  },

  {
      'name' : 'Sandrine',
      'lastname' : 'Bonjour',
      'username' : 'sandrine_bonjour',
      'password' : 'sandrine1234'
  },

    {
      'name' : 'Boit',
      'lastname' : 'deleau',
      'username' : 'boit_deleau',
      'password' : 'boit1234'
  }
]


for resp in dataRespEDT:
    ResponsableEdtService.create_responsable_edt(resp)


    