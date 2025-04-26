#Practica de como extraer informacion mediante BeautifulSoup
#Utilizar:  https://useplaintext.email/

import urllib.request, urllib.parse, urllib.error

from bs4 import BeautifulSoup

import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_name = ssl.CERT_NONE

while True:
    fname = input('Enter URL: ')
    if len(fname) < 1:
        print('Invalid URL. Try again, please. \n')
        continue
    break
    
url = urllib.request.urlopen(fname, context=ctx).read()

info = BeautifulSoup(url, 'html.parser')
data = info('p')

for item in data:
    print(item)
    