import urllib.request, urllib.parse, urllib.error

from bs4 import BeautifulSoup

import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_name = ssl.CERT_NONE

history = list()

while True:
    link = input("Insert link: ")
    if link == "":
        print("Invalid link. Try again, please.")
        print("")
        continue
    break
    
url = urllib.request.urlopen(link, context=ctx).read()

soup = BeautifulSoup(url, "html.parser")

tags = soup("a")

for tag in tags:
    x = tag.get("href", None)
    history.append(x)

    print(x)