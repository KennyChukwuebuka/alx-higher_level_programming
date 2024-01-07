#!/usr/bin/python3
"""script that takes in a url
   -sends a request to the url
   -display value of the variable X-Response-Id
"""

import requests
import sys

url = sys.argv[1]

response = requests.get(url)

if 'X-Request-Id' in response.headers:
    print("{}".format(response.headers['X-Request-Id']))
else:
    print("X-Request-Id variable not found in the response headers.")
