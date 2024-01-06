#!/usr/bin/python3
"""write a script that takes in a URL
   - sends a request to the URL
   -and displays the value of the X-Request-Id
"""
import urllib.request
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <URL>")
    else:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
                request_id = response.getheader('X-Request-Id')
                print("{}".format(request_id))
