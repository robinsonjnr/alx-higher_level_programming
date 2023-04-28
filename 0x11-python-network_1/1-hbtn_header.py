import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    request_id = response.getheader('X-Request-Id')

print(request_id)
