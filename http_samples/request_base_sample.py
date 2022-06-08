"""Sample HTTP commands"""
import random
from time import sleep

import requests

print("====================POST /user=========================")
# POST (add) user
user = {
  "id": random.randint(10000000, 99999999),
  "username": f"Lector{random.randint(10000000, 99999999)}",
  "firstName": "Denys",
  "lastName": "Kon",
  "email": "d13@dmail.com",
  "password": "133715678",
  "phone": "+374590057379",
  "userStatus": 0
}
URL = 'https://petstore.swagger.io/v2'
response = requests.request(method="POST", url=f"{URL}/user", json=user)
print(response.status_code)
print(response.text)
print("=" * 50)
sleep(3)

print("=====================GET /user====================")
# GET (read) user
response = requests.request(method="GET", url=f"{URL}/user/{user['username']}")
print(response.status_code)
print(response.text)
print("=" * 50)
sleep(3)

print("=====================PUT /user====================")
# PUT (edit) user
updated_user = {
  "id": user["id"],
  "firstName": "NewName",
  "phone": "+888888888888",
}
response = requests.request(method="PUT", url=f"{URL}/user/{user['username']}", json=updated_user)
print(response.status_code)
print(response.text)
print(response.reason)
print("=" * 50)
sleep(3)

print("=====================GET /user====================")
# GET (read) user
response = requests.request(method="GET", url=f"{URL}/user/{user['username']}")
print(response.status_code)
print(response.text)
print("=" * 50)
