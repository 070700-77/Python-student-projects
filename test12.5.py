import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import xml.etree.ElementTree as ET

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = []

while True:
    url = input("Enter url: ")
    if url == "":
        print("Enter a valid url. Try again")
        continue
    break
link = urllib.request.urlopen(url, context=ctx).read()
tree = ET.fromstring(link)

index = tree.findall('comments/comment')
for item in index:
    number = int(item.find('count').text)
    count.append(number)
print(f'Retrieving: {url}')
print(f'Count: {len(count)} \nSum: {sum(count)}')