#!/usr/bin/python3
"""
A Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

from sys import argv
import requests

if __name__ == "__main__":
    if argv[1]:
        q = argv[1]
    else:
        q = ""
    payload = {'q': q}
    response = requests.post("http://0.0.0.0:5000/search_user", data=q)
    try:
        response = response.json()
    except requests.exceptions.JSONDecodeError as e:
        print("Not a valid JSON")
    if response is None:
        print("No result")
    else:
        print("[{}] {}".format(response['id'], response['name']))
