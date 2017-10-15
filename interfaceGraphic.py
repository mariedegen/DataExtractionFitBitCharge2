# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Heart_Rate(object):
    
    def setupUi(self, Heart_Rate, nameGraphic):  
        Heart_Rate.setObjectName("Heart_Rate")
        Heart_Rate.resize(908, 318)
        Heart_Rate.setStyleSheet("border-image: url("+nameGraphic+");\n"
"border-color: rgb(0, 0, 0);")
        self.retranslateUi(Heart_Rate)
        QtCore.QMetaObject.connectSlotsByName(Heart_Rate)

    def retranslateUi(self, Heart_Rate):
        _translate = QtCore.QCoreApplication.translate
        Heart_Rate.setWindowTitle(_translate("Heart_Rate", "Dialog"))



