#!/usr/bin/python3
# Python script that takes in a URL, sends a request to the URL
# and displays the body of the response (decoded in utf-8).

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    req = Request(url)
    try:
        with urlopen(req) as page:
            print(page.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
