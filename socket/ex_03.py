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
a_tags = soup("a")
for a_tag in a_tags:
    print(a_tag.get("href", None))

p_tags = soup("p")
for p_tag in p_tags:
    print(p_tag.get_text())
