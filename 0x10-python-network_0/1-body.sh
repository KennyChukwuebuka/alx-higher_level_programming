#!/bin/bash
# cURL to the end
if [ $(curl -L -s -X HEAD -w "%{http_code}" "$1") == '200' ]; then curl -Ls "$1"; fi
