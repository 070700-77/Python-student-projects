import json

import urllib.request, urllib.error, urllib.parse

import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_name = ssl.CERT_NONE

while True:
    lname = input('Enter API URL: ')
    if len(lname) < 1:
        print("Enter a valid URL. Try again. \n")
        continue
    break

while True:
    word = input('Enter the word You are looking for: ')
    if len(word) < 1 or word == None:
        print('Invalid word. Try again \n')
        continue
    break
    
word = word.strip()

param = {}
param['q'] = word

url = lname + word

open_url =urllib.request.urlopen(url, context=ctx)

info = open_url.read().decode()

data = json.loads(info)

data = json.dumps(info, indent=4)

print(data)