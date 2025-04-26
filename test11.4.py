import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    link = input("Enter link: ")
    if link == "":
        print("Enter a valir URL. Try again please")
        print("")
        continue
    break


url = urllib.request.urlopen(link, context=ctx).read()
soup =BeautifulSoup(url, "html.parser")

tags = soup("a")
for tag in tags:
    print(tag)