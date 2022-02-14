from authlib.integrations.requests_client import OAuth1Auth
import requests
import hidden


def augment(url, url_params):
    secrets = hidden.oauth()

    auth = OAuth1Auth(
        client_id=secrets["consumer_key"],
        client_secret=secrets["consumer_secret"],
        token=secrets["token_key"],
        token_secret=secrets["token_secret"],
    )

    resp = requests.get(url, url_params, auth=auth)

    return resp
