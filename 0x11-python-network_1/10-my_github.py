#!/usr/bin/python3
"""
A Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
from sys import argv
import requests

if __name__ == "__main__":
    # payload = {'username': argv[1], 'password': argv[2]}
    headers = {
        'Accept': "application/vnd.github+json",
        'Authorization': "Bearer {}".format(argv[2]),
        'X-GitHub-Api-Version': "2022-11-28",
        }
    response = requests.get('https://api.github.com/user', headers=headers)
    print(response.json().get('id'))
