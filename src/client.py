import requests
import json
from collections import namedtuple

url = 'https://api-test.maxma.com/'
secret_key = "f8634ce0-5ca2-4b99-a371-110383cb3ecf"
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Cache-Control': 'no-cache',
  'X-Processing-Key': secret_key
}
phone = '+79774583897'

class Maxma():
  def __init__(self, url, secret_key, headers, phone):
    self.url = url
    self.secret_key = secret_key
    self.headers = headers
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
      return respDTO.bonuses[0].amount
    except IndexError:
      return 0

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

personOne = Maxma(url, secret_key, headers, phone)

print(personOne.get_balance())
# print(class1.add_new_client('+79774583895' ,'chetv@mail.ru', 'Mik CHetv', 1,
#                      '1998-11-21T00:00:00+04:00', '2222235'))
print(personOne.send_code())
# print(class1.change_balance(50))