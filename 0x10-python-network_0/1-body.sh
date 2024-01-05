#!/bin/bash
# cURL to the end
[ $# -eq 0 ] && echo "Usage: $0 <URL>" && exit 1; URL=$1; response=$(curl -s -o /dev/null -w "%{http_code}" "$URL"); [ "$response" == "200" ] && curl -s "$URL" || echo "Response code: $response. Body will not be displayed for non-200 status codes."
