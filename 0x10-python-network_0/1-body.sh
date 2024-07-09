#!/bin/bash
# A Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
echo "$(curl -sLI $1)" | grep -q "200 OK" && curl -sL $1
