#!/usr/bin/python
 
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

import interfaceMain
import graphicData
from interfaceGraphic import *
from interfaceChoice import *
 
class ImageViewer(QtWidgets.QMainWindow, interfaceMain.Ui_FitbitWindow):
    
    def __init__(self, parent=None):
        super(ImageViewer, self).__init__(parent)
        self.setupUi(self)

        #attribut the name of the user
        self.userName = ''        
        
        #handle the click
        self.btnCoeur.clicked.connect(self.handleButtonHeart)
        self.btnLocalisation.clicked.connect(self.handleButtonLocalisation)
        self.btnHomme.clicked.connect(self.handleButtonMen)
        self.btnPas.clicked.connect(self.handleButtonStep)
        self.btnFeu.clicked.connect(self.handleButtonFire)
        self.btnEscalier.clicked.connect(self.handleButtonStair)
        self.btnEclair.clicked.connect(self.handleButtonLightning)
        self.btnData.clicked.connect(self.handleButtonData)


    #To diplay the graph oh the heart rate in an other window
    def handleButtonHeart(self):
        #to create and to save the graph
        functionGraph = graphicData.CatalogFunction()
        graph = functionGraph.DisplayGraphHeart(self.userName)

        if(graph != None):
            self.windowGraph(graph)
        else:
            infoBox = QMessageBox()
            infoBox.setIcon(QMessageBox.Information)
            infoBox.setText("No data today or data not synchronized")
            infoBox.setWindowTitle("Data missing")
            infoBox.setEscapeButton(QMessageBox.Close)
            infoBox.exec_()

        """graphMonth = functionGraph.DisplayGraphHeartMonth(self.userName)
        windowGraph(graphMonth)"""
    
    def handleButtonLocalisation(self):
        print('PyQt5 button click 2 ')

    def handleButtonMen(self):
        print('PyQt5 button click 3 ')

    def handleButtonStep(self):
        functionGraph = graphicData.CatalogFunction()
        graph = functionGraph.DisplayGraphStep(self.userName)

        self.windowGraph(graph)

    def handleButtonFire(self):
        print('PyQt5 button click 5')

    def handleButtonStair(self):
        print('PyQt5 button click 6')

    def handleButtonLightning(self):
        print('PyQt5 button click 7')

    #To diplay the graph oh the heart rate in an other window
    def handleButtonData(self):
        #To create and to write a file
        functionGraph = graphicData.CatalogFunction()
        functionGraph.WriteFile(self.userName)

        #to display a message
        QMessageBox.about(self, "Data export", "Data exported !")

    #To display the image of the graphic
    def windowGraph(self, nameGraph):
        Heart_Rate = QtWidgets.QDialog()
        ui = Ui_Heart_Rate()
        ui.setupUi(Heart_Rate, nameGraph)
        Heart_Rate.exec_()

    """def showdialog(self):

        Choice_Heart = QtWidgets.QDialog()
        uiHeart = Ui_ChoiceHeart()
        uiHeart.setupUi(Choice_Heart)
        Choice_Heart.exec_()""" #a continuer        

    def main(self, nameUser):
        self.userName = nameUser
        self.show()


def mainInterface(nameUser):
        appFitbit = QtWidgets.QApplication([])
        imageViewer = ImageViewer()
        imageViewer.main(nameUser)
        sys.exit(appFitbit.exec_())
