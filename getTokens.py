
"""
Using the Authorization Code Grant

The inital code was producted by pdwhmeautomation in Python 2
This code has been adapted by Pauline LAURON for Python 3
"""

import base64
import urllib.request
import urllib.error
import json

#These are the secrets etc from Fitbit developer
OAuthTwoClientID = '228M93'
ClientOrConsumerSecret = '5ab70e6d954ba131b5928d272e3cf5e6'

#This is the Fitbit URL
TokenURL = 'https://api.fitbit.com/oauth2/token'

#I got this from the first verifier part when authorising my application
AuthorisationCode = "25115f85d5212a7138b6841d7ba09829fe2c570b"


#Form the data payload
BodyText = {'code' : AuthorisationCode,
            'redirect_uri' : 'https://www.google.fr',
            'client_id' : OAuthTwoClientID,
            'grant_type' : 'authorization_code'}

BodyURLEncoded = urllib.parse.urlencode(BodyText).encode('ascii')
print(BodyURLEncoded)

#Start the request
req = urllib.request.Request(TokenURL,BodyURLEncoded)

#Add the headers, first we base64 encode the client id and client secret with a : inbetween and create the authorisation header
req.add_header('Authorization', 'Basic ' + base64.b64encode((OAuthTwoClientID + ':' + ClientOrConsumerSecret).encode('ascii')).decode('utf-8'))
req.add_header('Content-Type', 'application/x-www-form-urlencoded')

#Fire off the request
try:
  response = urllib.request.urlopen(req)

  FullResponse = response.read()

  ResponseJSON = json.loads(FullResponse)

  print("Output >>> " + FullResponse.decode('utf-8'))
except urllib.error.URLError as e:
  print(e.code)
  print(e.read())
