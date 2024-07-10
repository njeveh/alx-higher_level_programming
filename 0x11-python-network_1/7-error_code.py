#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to
the URL and displays the body of the response.
"""
from sys import argv
import requests

if __name__ == "__main__":
    try:
        response = requests.get(argv[1])
        print(response.text)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(e.errno))
