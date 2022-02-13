import urllib.request
import urllib.parse
import urllib.error
import ssl
from twurl import augment

print("* Calling Twitter...")
url = augment("https://api.twitter.com/1.1/statuses/user_timeline.json", '')
print(url)

# Ignore SSl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

connection = urllib.request.urlopen(url, context=ctx)
data = connection.read()
print(data)

headers = dict(connection.getheaders())
print(headers)
