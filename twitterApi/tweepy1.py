import tweepy
import hidden
import json

secrets = hidden.oauth()
auth = tweepy.OAuthHandler(secrets["consumer_key"], secrets["consumer_secret"])
auth.set_access_token(secrets["token_key"], secrets["token_secret"])

api = tweepy.API(auth)

while True:
    acct = input("Enter Twitter Account:")
    if len(acct) < 1:
        break

    user = api.get_user(screen_name=acct)

    print(json.dumps(user, indent=2))
