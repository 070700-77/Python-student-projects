import urllib.request, urllib.parse, urllib.error

import ssl

from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_name = ssl.CERT_NONE

while True:
    link = input("Enter URL: ")
    if link == "":
        print("Enter a valid URL. Try again")
        print("")
        continue
    break

url = urllib.request.urlopen(link, context=ctx).read()
soup = BeautifulSoup(url, "html.parser")

print("")

tags = soup("a")
for tag in tags:
    print (tag.get("href", None))