import requests
import json

router = {
    "host": "10.10.20.48",
    "port": "443",
    "user": "developer",
    "password": "C1sco12345"
}

url = f"https://{router['host']}:{router['port']}/restconf/data/netconf-state/capabilities"

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

'''when I am making my request I want to store that response to variable called 'response',
using the request library i make a get request, will specify the url and headers which
equal the url and headers i created above. The basic authentication which is required by
device 'auth' equals the tuple that contains username and password sortied in dictionary 
above. also this http endpoint use self-signed certs so verify=False'''
response = requests.get(url=url, headers=headers, auth=(
    router['user'], router['password']), verify=False)

'''checking if response sttaus is 200, before converting json response to 
dictionary. '''
if response.status_code == 200:
    response_dict = response.json()
    '''because capability was is returning to im in array of capabilities i can use 
     for loop to loop over each of the responses and print them out one at the time, so i 
     can cleanly look at then that way   '''
    for capability in response_dict['ietf-netconf-monitoring:capabilities']['capability']:
        print(capability)
