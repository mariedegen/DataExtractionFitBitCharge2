# -*- coding: utf-8 -*-

import authentification
import imageViewer
import graphData

from PyQt5 import QtCore, QtGui, QtWidgets

#Connexion and get data
dataConnexion = authentification.mainAuthentification()

#Name of the user
nameUser = dataConnexion['user']['displayName']

#Open the application
windowFitbit = imageViewer.mainInterface(nameUser)

