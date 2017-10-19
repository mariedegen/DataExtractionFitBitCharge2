# -*- coding: utf-8 -*-

import authentification
import imageViewer

from PyQt5 import QtCore, QtGui, QtWidgets


def mainApp():
    
    print("ok")
    #Connexion and get profile data
    connexionProfile = authentification.mainAuthentification(0)

    print("ok")

    #Name of the user
    nameUser = connexionProfile['user']['displayName']


    print(nameUser)

    #Open the application
    windowFitbit = imageViewer.mainInterface(nameUser)


    print("ok")

