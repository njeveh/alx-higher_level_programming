#!/bin/bash
# A script that sends a request to a URL passed as an argument, and displays only the status code of the response.
curl "$1" -s -w "%{response_code}" -o /dev/null
