#!/usr/bin/python3
"""script that takes in a url
   -sends a request to the url
   -display value of the variable X-Response-Id
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

response = requests.get(url)

x_request_id = response.headers.get('X-Request-Id')
print("{}".format(x_request_id))
