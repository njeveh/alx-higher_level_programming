#!/usr/bin/python3
"""
A Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    url = "https://api.github.com/user"
    auth = HTTPBasicAuth(argv[1], argv[2])
    response = requests.get(url, auth=auth)
    print(response.json().get('id'))
