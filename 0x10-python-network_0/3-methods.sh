#!/bin/bash
# script that takes url and display all HTTP
curl -s -X OPTIONS -i "$1" | grep -i "allow:" | tr -d '\r' | awk '{$1=""; print $0}'
