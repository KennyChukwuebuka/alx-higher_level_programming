#!/usr/bin/python3
"""script that takes in a url
   -sends a request to the url
   -display value of the variable X-Response-Id
"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
