from ncclient import manager
import logging

logging.basicConfig(level=logging.DEBUG)

router = {
    "host": "sandbox-iosxr-1.cisco.com",
    "port": "830",
    "username": "admin",
    "password": "C1sco12345"
}

with manager.connect(**router, hostkey_verify=False) as m:
    print('hello world')
