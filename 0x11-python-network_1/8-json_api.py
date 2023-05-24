#!/usr/bin/python3
""" Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    data = {"q": sys.argv[1] if len(sys.argv) > 1 else ""}
    url = "http://0.0.0.0:5000/search_user"
    r = requests.post(url, data=data)
    try:
        json = r.json()
        if json:
            print("[{}] {}".format(json.get("id"), json.get("name")))
        else:
            print('No result')
    except Exception:
        print('Not a valid JSON')
