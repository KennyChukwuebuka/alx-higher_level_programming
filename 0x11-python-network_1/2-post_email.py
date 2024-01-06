#!/usr/bin/python3
"""Write script that takes in a URL and an email
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    try:
        with urllib.request.urlopen(url, data=data) as response:

            body = response.read().decode('utf-8')
            print("Response body:")
            print(body)
    except urllib.error.HTTPError as e:
        print("HTTP Error: {} - {}".format(e.code, e.reason))
    except urllib.error.URLError as e:
        print("URL Error: {}".format(e.reason))
