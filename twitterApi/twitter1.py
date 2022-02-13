import urllib.request
import urllib.parse
import urllib.error
import twurl
import json

TWITTER_URL = "https://api.twitter.com/1.1/statuses/user_timeline.json"

while True:
    print("")
    acct = input("Enter Twitter Account:")
    if len(acct) < 1:
        break
    url = twurl.augment(TWITTER_URL, {"screen_name": acct, "count": 2})
    print("Retrieving", url)
    http = urllib3.PoolManager()
    r = http.request("GET", url)
    print(json.loads(r.data.decode("utf-8")))
