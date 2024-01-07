#!/usr/bin/python3
"""script that fetch a url
"""

import requests

url = 'https://alx-intranet.hbtn.io/status'

response = requests.get(url)

response.status_code == 200

print("Body response")
print("\t- type:", type(response.text))
print("\t- content", response.text)
