import requests
import json
from collections import namedtuple


# secret_key = "f8634ce0-5ca2-4b99-a371-110383cb3ecf"
# phone = '89774583892'

class Maxma():
  def __init__(self, phone):
    self.url = 'https://api-test.maxma.com/'
    self.secret_key = 'f8634ce0-5ca2-4b99-a371-110383cb3ecf'
    self.headers = {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      'Cache-Control': 'no-cache',
      'X-Processing-Key': self.secret_key
    }
    self.phone = phone

  def to_dto(self, responce):
    x = json.loads(responce.text, object_hook 
                  = lambda d : namedtuple('X', d.keys())
                  (*d.values()))
    return x

  def get_balance(self):
    url = self.url + 'get-balance'
    data = {
      "phoneNumber": self.phone
    }
    r = requests.post(url=url,headers=self.headers, json=data)
    respDTO = self.to_dto(r)
    try:
      return respDTO
    except IndexError:
      return 0

  def add_new_client_short(self, phone, email, fullName, birthdate):
    url = self.url + 'new-client'
    data = {
      "client": {
        "phoneNumber": phone,
        "email": email,
        "fullName": fullName,
        "birthdate": birthdate
      }
    }
    r = requests.post(url=url, headers=self.headers, json=data)
    return self.to_dto(r)
  
  def add_new_client(self, phone, email, fullName, gender, birthdate, card):
    url = self.url + 'new-client'
    data = {
      "client": {
        "phoneNumber": phone,
        "email": email,
        "fullName": fullName,
        "gender": gender,
        "birthdate": birthdate,
        "card": card
      }
    }
    r = requests.post(url=url, headers=self.headers, json=data)
    return self.to_dto(r)

  def update_client(self, new_phone):
    url = self.url + 'update-client'
    data = {
      "phoneNumber": self.phone,
      "client": {
        "phoneNumber": new_phone
      }
    }
    r = requests.post(url=url, headers=self.headers, json=data)
    return self.to_dto(r)
    
    
  def send_code(self):
    url = self.url + 'send-confirmation-code'
    data = {
      "phoneNumber": self.phone
    }
    r = requests.post(url=url,headers=self.headers, json=data)
    respDTO = self.to_dto(r)
    return respDTO

  def change_balance(self, delta):   
    url = self.url + 'adjust-balance'
    data = {
      "client": {
        "phoneNumber": self.phone
      },
      "balanceAdjustment": {
        "amountDelta": delta,
        "expirationPeriodDays": 60,
        "comment": "компенсация за возврат по причине брака",
        "notify": True
      }
    }
    r = requests.post(url=url,headers=self.headers, json=data)
    respDTO = self.to_dto(r)
    return respDTO

# personOne = Maxma(phone)


# print(personOne.update_client("89774583897"))
# print(personOne.get_balance())
# print(personOne.add_new_client('+79774583822' ,'chetv@mail.ru', 'Mik CHetv', 1,
#                      '1998-11-21T00:00:00+04:00', '0'))
# print(personOne.send_code())
# print(personOne.change_balance(50))