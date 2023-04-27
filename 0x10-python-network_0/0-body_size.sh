#!/bin/bash
# Take URL as input and send request and store response in a variable

read -p "Enter URL: " url
response=$(curl -s $url)
size=$(echo -n "$response" | wc -c)
echo "Size of response body: $size bytes"

