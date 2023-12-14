from scrapli_netconf.driver import NetconfScrape

my_device = {
    "host": "10.10.20.48",
    "auth_username": "developer",
    "auth_password": "C1sco12345",
    "auth_strict_key": False,
    "port": 830
}

conn = NetconfScrape(**my_device)
conn.open()

ospf_filter = """
<ospf-oper-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf-oper">
  <ospf-state>
 
</ospf-oper-data>
"""

response = conn.get(
    filter_=ospf_filter, filter_type='subtree')
print(response.result)
