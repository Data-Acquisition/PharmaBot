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

def to_dto(responce):
  x = json.loads(responce.text, object_hook 
                 = lambda d : namedtuple('X', d.keys())
                 (*d.values()))
  return x

def get_balance(url, phone):
  url += 'get-balance'
  data = {
    "phoneNumber": phone
  }
  data_json = json.dumps(data)
  r = requests.post(url=url,headers=headers, data=data_json)
  respDTO = to_dto(r)
  return respDTO.bonuses[0]

def add_new_client(url, phone, email, fullName, gender, birthdate, card):
  url += 'new-client'
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
  data_json = json.dumps(data)
  r = requests.post(url=url,headers=headers, data=data_json)
  return to_dto(r)

def send_code(url, phone):
  url += 'send-confirmation-code'
  data = {
    "phoneNumber": phone
  }
  data_json = json.dumps(data)
  r = requests.post(url=url,headers=headers, data=data_json)
  respDTO = to_dto(r)
  return respDTO

def change_balance(url, phone, delta):
  url += 'adjust-balance'
  data = {
    "client": {
      "phoneNumber": phone
    },
    "balanceAdjustment": {
      "amountDelta": delta,
      "expirationPeriodDays": 60,
      "comment": "компенсация за возврат по причине брака",
      "notify": True
    }
  }
  data_json = json.dumps(data)
  r = requests.post(url=url,headers=headers, data=data_json)
  respDTO = to_dto(r)
  return respDTO

print(add_new_client(url, '+79774583899', 'mike@mail.ru', 'Mike CH', 1,
                     '1999-11-21T00:00:00+04:00', '22222').description)

print(get_balance(url,'+375296300643'))
print(get_balance(url,'+79534706854'))
# print(send_code(url, '+79774583897'))
# print(change_balance(url, '+79774583897', 400))