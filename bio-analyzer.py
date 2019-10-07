from urllib.request import urlopen
import json
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

def send_text():
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message_text = "Tattoo is a gooooooooo! https://www.instagram.com/melaniesteinway"
    message = client.messages.create(to="+13104158457", from_='+112015813048', body=message_text)

def get_jsonparsed_data(url):
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

url = ("https://www.instagram.com/melaniesteinway/?__a=1")
result = get_jsonparsed_data(url)
bio= result['graphql']['user']['biography']

if "BOOKS CLOSED" in bio:
    exit()
else:
    send_text()