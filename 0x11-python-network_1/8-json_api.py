#!/usr/bin/python3
"""
A Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

from sys import argv
import requests

if __name__ == "__main__":
    q = ''
    if len(argv) > 1:
        q = argv[1]
    payload = {'q': q}
    response = requests.post("http://0.0.0.0:5000/search_user", data=q)
    try:
        response = response.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get('id'), response.get('name')))
    except ValueError:
        print("Not a valid JSON")
