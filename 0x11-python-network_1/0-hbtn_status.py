#!/usr/bin/python3
# Python script that fetches https://alx-intranet.hbtn.io/status

from urllib.request import Request, urlopen
from urllib.error import URLError

url = "https://alx-intranet.hbtn.io/status"
with urlopen(url) as page:
    data = page.read()
    print('Body response:')
    print('\t- type: {}'.format(type(data)))
    print('\t- content: {}'.format(data))
    print('\t- utf8 content: {}'.format(data.decode('utf-8')))
