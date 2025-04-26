import urllib.request, urllib.error, urllib.parse

import json

import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_name = ssl.CERT_NONE


while True:
    base_url = input("Enter URL:")
    if len(base_url)<1:
        print("Try again please. \n")
        continue
    break
    
url = urllib.request.urlopen(base_url, context =ctx)

info = url.read().decode()

data = json.loads(info)

organized_data = json.dumps(data, indent=4)

print(organized_data)