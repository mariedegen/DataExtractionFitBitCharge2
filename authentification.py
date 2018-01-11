"""

Using the Authorization Code Grant

The inital code was producted by pdwhmeautomation in Python 2
This code has been adapted by Pauline LAURON for Python 3
"""

import base64
import urllib.request
import urllib.error
import sys
import json
import os
import bs4

import getTokens

#This is the Fitbit URL to use for the API call
FitbitURLProfile = "https://api.fitbit.com/1/user/-/profile.json"
FitbitURLHeart = "https://api.fitbit.com/1/user/-/activities/heart/date/today/1d/1min.json"
FitbitURLStep = "https://api.fitbit.com/1/user/-/activities/steps/date/today/1m.json"
FitbitURLFloor = "https://api.fitbit.com/1/user/-/activities/floors/date/today/1m.json"
FitbitURLCalories = "https://api.fitbit.com/1/user/-/activities/calories/date/today/1m.json"
FitbitURLDistance = "https://api.fitbit.com/1/user/-/activities/distance/date/today/1m.json"
FitbitURLMinutes = "https://api.fitbit.com/1/user/-/activities/minutesSedentary/date/today/1m.json"
FitbitURLActive = "https://api.fitbit.com/1/user/-/activities/minutesVeryActive/date/today/1m.json"

# apiCall = '/1/user/-/devices.json'
# apiCall = '/1/user/-/activities/date/2015-10-22.json'

#Use this URL to refresh the access token
TokenURL = "https://api.fitbit.com/oauth2/token"

#Get and write the tokens from here
IniFile = "tokens.txt"

#From the developer site
OAuthTwoClientID = "228M93"
ClientOrConsumerSecret = "5ab70e6d954ba131b5928d272e3cf5e6"

#Some contants defining API error handling responses
TokenRefreshedOK = "Token refreshed OK"
ErrorInAPI = "Error when making API call that I couldn't handle"

#Get the config from the config file.  This is the access and refresh tokens
def GetConfig():
  print("Reading from the config file")

  #Open the file
  FileObj = open(IniFile,'r')

  #Read first two lines - first is the access token, second is the refresh token
  AccToken = FileObj.readline()
  RefToken = FileObj.readline()

  #Close the file
  FileObj.close()

  #See if the strings have newline characters on the end.  If so, strip them
  if (AccToken.find("\n") > 0):
    AccToken = AccToken[:-1]
  if (RefToken.find("\n") > 0):
    RefToken = RefToken[:-1]

  #Return values
  return AccToken, RefToken

def WriteConfig(AccToken,RefToken):
  print("Writing new token to the config file")
  print("Writing this: " + AccToken + " and " + RefToken)

  #Delete the old config file
  os.remove(IniFile)

  #Open and write to the file
  FileObj = open(IniFile,'w')
  FileObj.write(AccToken + "\n")
  FileObj.write(RefToken + "\n")
  FileObj.close()

#Make a HTTP POST to get a new
def GetNewAccessToken(RefToken):
  print("Getting a new access token")

  #Form the data payload
  BodyText = {'grant_type' : 'refresh_token',
              'refresh_token' : RefToken}
  #URL Encode it
  BodyURLEncoded = urllib.parse.urlencode(BodyText).encode('utf-8')
  print("Using this as the body when getting access token >>" + BodyURLEncoded.decode('ascii'))

  #Start the request
  tokenreq = urllib.request.Request(TokenURL,BodyURLEncoded)

  #Add the headers, first we base64 encode the client id and client secret with a : inbetween and create the authorisation header
  tokenreq.add_header('Authorization', 'Basic ' + base64.b64encode((OAuthTwoClientID + ':' + ClientOrConsumerSecret).encode('ascii')).decode('utf-8'))
  tokenreq.add_header('Content-Type', 'application/x-www-form-urlencoded')

  #Fire off the request
  try:
    tokenresponse = urllib.request.urlopen(tokenreq)
  
    #See what we got back.  If it's this part of  the code it was OK
    FullResponse = tokenresponse.read()

    #Need to pick out the access token and write it to the config file.  Use a JSON manipluation module
    ResponseJSON = json.loads(FullResponse)

    print(ResponseJSON)

    #Read the access token as a string
    NewAccessToken = str(ResponseJSON['access_token'])
    NewRefreshToken = str(ResponseJSON['refresh_token'])
    #Write the access token to the ini file
    WriteConfig(NewAccessToken,NewRefreshToken)

    print("New access token output >>> " + FullResponse.decode('utf-8'))
    
  except urllib.error.URLError as e:
    #Gettin to this part of the code means we got an error
    print("An error was raised when getting the access token.")
    print(e.code)
    print(e.read())

    #To get a new first token
    getTokens.getFirstToken(IniFile)
    mainAuthentification(0)
    
    #sys.exit()

#This makes an API call.  It also catches errors and tries to deal with them
def MakeAPICall(InURL,AccToken,RefToken):
  #Start the request
  req = urllib.request.Request(InURL)

  #Add the access token in the header
  req.add_header('Authorization', 'Bearer ' + AccToken)

  print("I used this access token " + AccToken)


  #Fire off the request
  try:
    #Do the request
    response = urllib.request.urlopen(req)

    #Read the response
    FullResponse = json.load(response)

    #print(FullResponse)
    
    #Return values
    return True, FullResponse
  #Catch errors, e.g. A 401 error that signifies the need for a new access token
  except urllib.error.HTTPError as e:
    print(e.code)
    print("Got this HTTP error: " + str(e.code))
    HTTPErrorMessage = e.read().decode("utf8","ignore")
    print("This was in the HTTP error message: " + HTTPErrorMessage)
    #See what the error was    
    if (e.code == 401): #and (HTTPErrorMessage.find("Access token invalid or expired") > 0):
      GetNewAccessToken(RefToken)
      return False, TokenRefreshedOK
    #Return that this didn't work, allowing the calling function to handle it
    return False, ErrorInAPI


#Main part of the code
def mainAuthentification(menu):
  #Declare these global variables that we'll use for the access and refresh tokens
  AccessToken = ""
  RefreshToken = ""

  print("Fitbit API Test Code")

  #Get the config
  AccessToken, RefreshToken = GetConfig()

  #Make the API call
  if (menu == 0):
    APICallOK, APIResponse = MakeAPICall(FitbitURLProfile, AccessToken, RefreshToken)
  elif (menu == 1):
    APICallOK, APIResponse = MakeAPICall(FitbitURLHeart, AccessToken, RefreshToken)
  elif (menu == 2):
    APICallOK, APIResponse = MakeAPICall(FitbitURLStep, AccessToken, RefreshToken)
  elif (menu == 3):
    APICallOK, APIResponse = MakeAPICall(FitbitURLFloor, AccessToken, RefreshToken)
  elif (menu == 4):
    APICallOK, APIResponse = MakeAPICall(FitbitURLCalories, AccessToken, RefreshToken)
  elif (menu == 5):
    APICallOK, APIResponse = MakeAPICall(FitbitURLDistance, AccessToken, RefreshToken)
  elif (menu == 6):
    APICallOK, APIResponse = MakeAPICall(FitbitURLMinutes, AccessToken, RefreshToken)
  elif (menu == 7):
    APICallOK, APIResponse = MakeAPICall(FitbitURLActive, AccessToken, RefreshToken)
  else :
    APICallOK, APIResponse = MakeAPICall(FitbitURLProfile, AccessToken, RefreshToken)

  if APICallOK:
    return APIResponse
  else:
    if (APIResponse == TokenRefreshedOK):
      print("Refreshed the access token.  Can go again")
      AccessToken, RefreshToken = GetConfig()
      APICallOK, APIResponse = MakeAPICall(FitbitURLProfile, AccessToken, RefreshToken)
      if APICallOK:
        return APIResponse
      else:
        print(ErrorInAPI)
    else:
     print(ErrorInAPI)

  
