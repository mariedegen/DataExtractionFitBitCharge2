
"""
Using the Authorization Code Grant

The inital code was producted by pdwhmeautomation in Python 2
This code has been adapted by Pauline LAURON for Python 3
"""

import base64
import urllib.request
import urllib.error
import json


def getFirstToken(tokenFileName):

  #These are the secrets etc from Fitbit developer
  OAuthTwoClientID = '228M93'
  ClientOrConsumerSecret = '5ab70e6d954ba131b5928d272e3cf5e6'

  #This is the Fitbit URL
  TokenURL = 'https://api.fitbit.com/oauth2/token'

  #URL to get the authorisation code
  Auth_URL = "https://www.fitbit.com/oauth2/authorize?response_type=code&client_id=228M93&redirect_uri=https%3A%2F%2Fwww.google.fr&scope=activity%20heartrate%20location%20nutrition%20profile%20settings%20sleep%20social%20weight&expires_in="

  print("Go to the URL : \n%s" % Auth_URL)

  #To get tokens
  AuthorisationCode = input("Put your fitbit's id to be connected. Copy the XXXX part of the URL https://www.google.fr/?code=XXXXXXXXXXXXXXXXXXXXXXX#_=_ here : ")

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

    accessToken = ResponseJSON['access_token']
    refreshToken = ResponseJSON['refresh_token']

    tokenFile = open(tokenFileName, "w")
    tokenFile.write(accessToken)
    tokenFile.close()

    tokenFile = open(tokenFileName, "a")
    tokenFile.write("\n" + refreshToken)
    tokenFile.close()
    
  except urllib.error.URLError as e:
    print(e.code)
    print(e.read())

