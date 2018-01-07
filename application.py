# -*- coding: utf-8 -*-

import authentification
import imageViewer

from PyQt5 import QtCore, QtGui, QtWidgets
    
#Connexion and get profile data
connexionProfile = authentification.mainAuthentification(0)

#Name of the user
nameUser = connexionProfile['user']['displayName']

#Open the application
imageViewer.mainInterface(nameUser)



