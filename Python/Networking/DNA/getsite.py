import requests
import json

base_url = "https://sandboxdnac2.cisco.com/dna/"
auth_endpoint = "system/api/v1/auth/token"
user = 'devnetuser'
pw = 'Cisco123!'
auth_response = requests.post(
    url=f"{base_url}{auth_endpoint}",
    auth=(user, pw)).json()
token = auth_response['Token']
headers = {
    "x-auth-token": token,
    "Accept": "application/json",
    "Content-Type": "application/json"
}
site_endpoint = "intent/api/v1/site"
site_response = requests.get(
    url=f"{base_url}{site_endpoint}", headers=headers).json()

print(json.dumps(site_response, indent=2))
