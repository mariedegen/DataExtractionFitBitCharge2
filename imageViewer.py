#!/usr/bin/python
 
from PyQt5 import QtGui, QtCore, QtWidgets
import sys

import interface
import graphData
 
class ImageViewer(QtWidgets.QMainWindow, interface.Ui_FitbitWindow):

    userName = ''
    
    def __init__(self, parent=None):
        super(ImageViewer, self).__init__(parent)
        self.setupUi(self)

        #handle the click
        self.btnCoeur.clicked.connect(self.handleButtonHeart)
        self.btnLocalisation.clicked.connect(self.handleButtonLocalisation)
        self.btnHomme.clicked.connect(self.handleButtonMen)
        self.btnPas.clicked.connect(self.handleButtonStep)
        self.btnFeu.clicked.connect(self.handleButtonFire)
        self.btnEscalier.clicked.connect(self.handleButtonStair)
        self.btnEclair.clicked.connect(self.handleButtonLightning)
        self.btnData.clicked.connect(self.handleButtonData)


    def handleButtonHeart(self):
        print('PyQt5 button click 1')

    def handleButtonLocalisation(self):
        print('PyQt5 button click 2 ')

    def handleButtonMen(self):
        print('PyQt5 button click 3 ')

    def handleButtonStep(self):
        print('PyQt5 button click 4')

    def handleButtonFire(self):
        print('PyQt5 button click 5')

    def handleButtonStair(self):
        print('PyQt5 button click 6')

    def handleButtonLightning(self):
        print('PyQt5 button click 7')

    def handleButtonData(self):
        graphData.writeGlobalJson(self, jsonFile, name)
       

        

 
    def main(self, nameUser):
        self.show()
        userName = nameUser

def mainInterface(nameUser): 
#if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    imageViewer = ImageViewer()
    imageViewer.main(nameUser)
    app.exec_()
