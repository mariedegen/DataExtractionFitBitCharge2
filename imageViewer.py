"""@package fitbit
The controller of the fitbit view (interfaceFitbit.py)
"""
 
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

import interfaceFitbit
import graphicData
from interfaceGraphic import *
from interfaceChoice import *
 
class ImageViewer(QtWidgets.QMainWindow, interfaceFitbit.Ui_FitbitWindow):
    """
        The controller class of the fitbit view
        :param QtWidgets.QMainWindow: the type of the main window
        :param interfaceFitbit.Ui_FitbitWindow: to leak with the view 
    """
    
    def __init__(self, parent=None):
        """
            To initialize the window
            :param self: the object
            :param parent: the parent of the window
        """
        super(ImageViewer, self).__init__(parent)
        self.setupUi(self)

        #attribut the name of the user
        self.userName = ''
        
        self.functionGraph = graphicData.CatalogFunction()
        
        #handle the click
        self.btnCoeur.clicked.connect(self.handleButtonHeart)
        self.btnLocalisation.clicked.connect(self.handleButtonLocalisation)
        self.btnHomme.clicked.connect(self.handleButtonMen)
        self.btnPas.clicked.connect(self.handleButtonStep)
        self.btnFeu.clicked.connect(self.handleButtonCalories)
        self.btnEscalier.clicked.connect(self.handleButtonFloor)
        self.btnEclair.clicked.connect(self.handleButtonLightning)
        self.btnData.clicked.connect(self.handleButtonData)
        self.menuHome.triggered[QAction].connect(self.closeIt)

    def handleButtonHeart(self):
        """
            To diplay the graph of the heart rate in an other window
        """
        #to create and to save the graph
        graph = self.functionGraph.GetGraphHeart(self.userName)

        if(graph != None):
            self.windowGraph(graph)
        else:
            infoBox = QMessageBox()
            infoBox.setIcon(QMessageBox.Information)
            infoBox.setText("No data today or data not synchronized")
            infoBox.setWindowTitle("Data missing")
            infoBox.setEscapeButton(QMessageBox.Close)
            infoBox.exec_()
    
    def handleButtonLocalisation(self):
        """
            To diplay the graph of the distance in an other window
        """
        graph = self.functionGraph.GetGraphDistance(self.userName)

        self.windowGraph(graph)

    def handleButtonMen(self):
        """
            To diplay the graph of the very active minutes in an other window
        """
        graph = self.functionGraph.GetGraphActive(self.userName)

        self.windowGraph(graph)

    def handleButtonStep(self):
        """
            To diplay the graph of the steps in an other window
        """
        graph = self.functionGraph.GetGraphStep(self.userName)

        self.windowGraph(graph)

    def handleButtonCalories(self):
        """
            To diplay the graph of the calories in an other window
        """
        graph = self.functionGraph.GetGraphCalories(self.userName)

        self.windowGraph(graph)

    def handleButtonFloor(self):
        """
            To diplay the graph of the number of the floor in an other window
        """
        graph = self.functionGraph.GetGraphFloor(self.userName)

        self.windowGraph(graph)

    def handleButtonLightning(self):
        """
            To diplay the graph of the minutes in move in an other window
        """
        graph = self.functionGraph.GetGraphMinutes(self.userName)

        self.windowGraph(graph)


    def handleButtonData(self):
        """
            To collect and export data
        """
        #To create and to write a file
        self.functionGraph.WriteFile(self.userName)

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

    """def showdialog(self):

        Choice_Heart = QtWidgets.QDialog()
        uiHeart = Ui_ChoiceHeart()
        uiHeart.setupUi(Choice_Heart)
        Choice_Heart.exec_()""" #a continuer        


    def closeIt(self, q):
        self.close()

    def main(self, nameUser):
        """
            To diplay the main window
        """
        self.userName = nameUser
        self.show()


def mainInterface(nameUser):
    """
       To run the fitbit application
       :param nameUser: The name of the user 
    """
    appFitbit = QtWidgets.QApplication([])
    imageViewer = ImageViewer()
    imageViewer.main(nameUser)
    sys.exit(appFitbit.exec_())
