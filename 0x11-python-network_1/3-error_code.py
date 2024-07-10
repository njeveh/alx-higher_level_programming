#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""
from sys import argv
import urllib.error
import urllib.request
import urllib.parse

if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: ', e.code)
    # except urllib.error.URLError as e:
    #     print('We failed to reach a server.')
    #     print('Reason: ', e.reason)
