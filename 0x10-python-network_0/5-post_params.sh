able file 3 lines (3 sloc) 157 Bytes
#!/bin/bash
#Sends a POST request to the passed URL with data
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
