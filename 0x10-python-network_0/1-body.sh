#!/bin/bash
# A Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
echo "$(curl -sLI $1)" | grep -q "200 OK" && curl -sL $1
