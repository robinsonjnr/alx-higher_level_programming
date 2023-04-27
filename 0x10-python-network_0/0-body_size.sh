#!/bin/bash
# Take URL as input and send request and store response in a variable
curl -s $1 | wc -c | awk -v size=$(curl -sI $1 | awk

