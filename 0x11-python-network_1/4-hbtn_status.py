#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status"""

import requests

if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    html = response.text
    print('Body response:')
    print('\t- type: {}'.format(type(html)))
    print('\t- content: {}'.format(html))
