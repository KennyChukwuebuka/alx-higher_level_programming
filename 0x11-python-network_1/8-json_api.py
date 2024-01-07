#!/usr/bin/python3
"""script that takes in a letter and sends a POST request to
- the URL http://0.0.0.0:5000/search_user with the letter as a parameter
- The letter must be sent in the variable q
- If no argument is given, set q=""
- If the response body is properly JSON formatted and not empty,
- display the id and name like this: [<id>] <name>
otherwise: Display Not a valid JSON if the JSON is invalid
Display No result if the JSON is empty
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        j = r.json()
        if j:
            print("[{}] {}".format(j.get('id'), j.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
