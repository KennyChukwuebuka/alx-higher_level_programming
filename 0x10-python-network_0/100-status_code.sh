#!/bin/bash
# script that sends a request to a URL passed as an argument and display status code
curl -L -s -X HEAD -w "%{http_code}" "$1"
