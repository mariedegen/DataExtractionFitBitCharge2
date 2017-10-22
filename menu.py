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

        self._want_to_close = False

        #handle the click
        self.pushButton.clicked.connect(self.handleButtonFitbit)
        self.pushButton_2.clicked.connect(self.handleButtonSamsung)


    #To diplay the graph oh the heart rate in an other window
    def handleButtonFitbit(self):
        applicationFitbit.mainApp()           

    def handleButtonSamsung(self):
        applicationSamsung.mainAppSamsung()  

    def main(self):
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    menu = Menu()
    menu.main()
