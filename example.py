#!/usr/bin/env python 

# simple example script that uses the login dialog to get a list of your gog games
# see https://gogapidocs.readthedocs.io/ for more info about the API

import subprocess
import requests
import urllib.parse
import json

# this is the path to the login runtime
RUNTIME='./target/release/goglogin'

# these are used by Gog in a few places
client_id='46899977096215655'
client_secret='9d85c43b1482497dbbce61f6e4aa173a433796eeae2ca8c5f6129f2dc4de46d9'
redirect_url='https://embed.gog.com/on_login_success?origin=client'

# show login screen, get initial tokens
def login():
  code = subprocess.run(RUNTIME, stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
  return json.loads(requests.get(f'https://auth.gog.com/token?client_id={client_id}&client_secret={client_secret}&grant_type=authorization_code&code={code}&redirect_uri={urllib.parse.quote(redirect_url)}').text)

# get fresh token with a refresh token
def refresh(refresh_token):
  return json.loads(requests.get(f'https://auth.gog.com/token?client_id={client_id}&client_secret={client_secret}&grant_type=refresh_token&refresh_token={refresh_token}').text)

# get list of owned game IDs
def owned(access_token):
  return json.loads(requests.get(f'https://embed.gog.com/user/data/games', headers={'Authorization': f'Bearer {access_token}'}).text)['owned']

# get details about game ID
def details(access_token, id):
  return json.loads(requests.get(f'https://embed.gog.com/account/gameDetails/{id}.json', headers={'Authorization': f'Bearer {access_token}'}).text)


tokens = login()
# tokens = refresh(tokens['refresh_token'])

for id in owned(tokens['access_token']):
  data = details(tokens['access_token'], id)
  print(data['title'])
