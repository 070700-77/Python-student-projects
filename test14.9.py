# Works with> https://api.genderize.io
import json

import urllib.request, urllib.parse, urllib.error

import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_name = ssl.CERT_NONE

while True:
    lname = input("Enter link: ")
    if len(lname) < 1:
        print("Invalid URL. Try again. \n")
        continue
    break
    
while True:
    pname = input("Enter the name you want to know it gender: ")
    if len(pname) < 1:
        print("Invalid name. Try again. \n")
        continue
    break   

params = {}
params["name"] = pname

query_string = urllib.parse.urlencode(params)

if "?" in lname:
    full_url = lname + "&" + query_string
else:
    full_url = lname + "?" + query_string
    
link = urllib.request.urlopen(full_url, context=ctx)
info = link.read().decode()

data = json.loads(info)

sorted_data = json.dumps(data, indent = 4)
print(sorted_data)