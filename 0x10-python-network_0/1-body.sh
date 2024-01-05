#!/bin/bash
# cURL to the end
[ $# -eq 0 ] && echo "Usage: $0 <URL>" && exit 1; curl -s "$1" | grep -o "Route 2"
