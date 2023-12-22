import requests
import json

base_url = "https://sandboxdnac2.cisco.com/dna/"
auth_endpoint = "system/api/v1/auth/token"

user = 'devnetuser'
password = 'Cisco123!'

''' i want to hold response from the post request in variable auth_response because i need
ro parse out the token'''
auth_response = requests.post(url=f"{base_url}{auth_endpoint}",
                               auth=(user, password)).json()

''' i save the respnse token in variab;le token for the latest use. from the  auth_response
grap the key 'Token'''
token = auth_response['Token']

''' building my headers now so I can use that token later'''
headers = {
    "x-auth-token": token,
    "Accept": "application/json",
    "Content-Type":"application/json"
}

print(token)

