#!/bin/bash
# script that takes url and display all HTTP
curl -s -I -X OPTIONS "$1" | grep 'Allow:' | cut -f2- -d' '
