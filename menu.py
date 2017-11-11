#!/usr/bin/python


"""
import pdb; pdb.set_trace()
"""

from PyQt5 import QtGui, QtCore, QtWidgets
import sys

import menuInterface
import applicationFitbit
import applicationSamsung
 
class Menu(QtWidgets.QDialog, menuInterface.Ui_Menu):
    
    def __init__(self, parent=None):
        super(Menu, self).__init__(parent)
        self.setupUi(self)

        #handle the click
        self.pushButton.clicked.connect(self.handleButtonFitbit)
        self.pushButton_2.clicked.connect(self.handleButtonSamsung)


    #To diplay the graph oh the heart rate in an other window
    def handleButtonFitbit(self):
        self.hide()
        applicationFitbit.mainApp()
        
    def handleButtonSamsung(self):
        self.hide()
        applicationSamsung.mainAppSamsung()  

    def main(self):
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    menu = Menu()
    menu.main()
