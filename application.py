# -*- coding: utf-8 -*-

import authentification
import imageViewer

from PyQt5 import QtCore, QtGui, QtWidgets

#Connexion and get data
dataConnexion = authentification.mainAuthentification()

nameUser = dataConnexion['user']['displayName']

print(nameUser)


#Open the application
windowFitbit = imageViewer.mainInterface()

