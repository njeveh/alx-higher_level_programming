#!/bin/bash
#A Bash script that takes in a URL and displays all HTTP methods the server will accept
curl -sIL "$1" | grep -i "Allow" | awk '{print substr($0, index($0, $2))}'
