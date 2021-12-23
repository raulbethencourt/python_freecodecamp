import urllib.request
import urllib.parse 
import urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificatte errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrive all
tags = soup("a")
for tag in tags:
    print(tag.get("href", None))
