import requests
import json

router = {
    "host": "10.10.20.48",
    "port": "443",
    "user": "developer",
    "password": "C1sco12345"
}

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

url = f"https://{router['host']}:{router['port']}/restconf/data/ietf-routing:routing"

response = requests.get(url=url, headers=headers, auth=(
    router['user'], router['password']), verify=False).json()

print(json.dumps(response, indent=2))

# url = f"https://{router['host']}:{router['port']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/"

# response = requests.get(url=url, headers=headers, auth=(
#     router['user'], router['password']), verify=False).json()

# print(json.dumps(response, indent=2))
