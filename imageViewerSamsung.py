"""@package fitbit
The controller of the samsung view (interfaceSamsung.py)
"""
 
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

import interfaceSamsung
import graphicData
from interfaceGraphic import *
 
class ImageViewerSamsung(QtWidgets.QMainWindow, interfaceSamsung.Ui_SamsungWindow):
    """
        The controller class of the fitbit view
        :param QtWidgets.QMainWindow: the type of the main window
        :param interfaceSamsung.Ui_SamsungWindow: to leak with the view 
    """
    
    def __init__(self, parent=None):
        """
            To initialize the window
            :param self: the object
            :param parent: the parent of the window
        """
        super(ImageViewerSamsung, self).__init__(parent)
        self.setupUi(self)

        #attribut the name of the user
        self.userName = ''

        self.functionGraph = graphicData.CatalogFunction()
        
        #handle the click
        self.btnCoeur.clicked.connect(self.handleButtonHeart)
        self.btnData.clicked.connect(self.handleButtonData)


    def handleButtonHeart(self):
        """
            To diplay the graph of the heart rate in an other window
        """
        print("working on...")


    def handleButtonData(self):
        """
            To collect and export data
        """
        print("working on...")

    def windowGraph(self, nameGraph):
        """
            To diplay the image of the graphe nameGraph
            :param nameGraph: the name of the graph
        """
        Heart_Rate = QtWidgets.QDialog()
        ui = Ui_Heart_Rate()
        ui.setupUi(Heart_Rate, nameGraph)
        Heart_Rate.exec_()

    def main(self):
        """
            To diplay the main window
        """
        self.show()


def mainInterface():
    """
       To run the samusung application
    """
    appSamsung = QtWidgets.QApplication([])
    imageViewerSamsung = ImageViewerSamsung()
    imageViewerSamsung.main()
    sys.exit(appSamsung.exec_())
