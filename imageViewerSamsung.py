"""@package fitbit
The controller of the samsung view (interfaceSamsung.py)
"""
 
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

import threading
from multiprocessing import Queue

import interfaceSamsung
import graphicData
import client_network
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

        #attribut the data array
        self.data = []

        self.functionGraph = graphicData.CatalogFunction()

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
        if (self.data == []):
            infoBox = QMessageBox()
            infoBox.setIcon(QMessageBox.Information)
            infoBox.setText("No data or data not synchronized yet")
            infoBox.setWindowTitle("Data missing")
            infoBox.setEscapeButton(QMessageBox.Close)
            infoBox.exec_()
        else:
            graph = self.functionGraph.GetGraphHeartSamsung(self.data)
            self.windowGraph(graph)
        

    def handleButtonData(self):
        """
            To collect and export data
        """
         #To create and to write a file
        self.functionGraph.WriteFileSamsung(self.data)

        #to display a message
        QMessageBox.about(self, "Data export", "Data exported !")

        
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

        #print(client_network.clientNetwork())

        """data = my_queue.get()
        print(data)"""
        

def mainInterface():
    """
       To run the samusung application
    """
    appSamsung = QtWidgets.QApplication([])
    imageViewerSamsung = ImageViewerSamsung()

    my_queue = Queue()
    thread1 = threading.Thread(target = client_network.clientNetwork, args = (imageViewerSamsung,))
    thread1.start()
            
    imageViewerSamsung.main()
    sys.exit(appSamsung.exec_())
