# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChoiceHeart(object):
    def setupUi(self, Choice_Heart):
        Choice_Heart.setObjectName("Choice_Heart")
        Choice_Heart.resize(464, 235)
        self.checkBox = QtWidgets.QCheckBox(Choice_Heart)
        self.checkBox.setGeometry(QtCore.QRect(60, 80, 241, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Choice_Heart)
        self.checkBox_2.setGeometry(QtCore.QRect(60, 110, 351, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Choice_Heart)
        self.checkBox_3.setGeometry(QtCore.QRect(60, 140, 231, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.label = QtWidgets.QLabel(Choice_Heart)
        self.label.setGeometry(QtCore.QRect(70, 30, 301, 31))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Choice_Heart)
        self.pushButton.setGeometry(QtCore.QRect(190, 180, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.handleButtonOk)

        self.retranslateUi(Choice_Heart)
        QtCore.QMetaObject.connectSlotsByName(Choice_Heart)

    def retranslateUi(self, Choice_Heart):
        _translate = QtCore.QCoreApplication.translate
        Choice_Heart.setWindowTitle(_translate("Choice_Heart", "Dialog"))
        self.checkBox.setText(_translate("Choice_Heart", "Display the graphic of today\'s heart rate"))
        self.checkBox_2.setText(_translate("Choice_Heart", "Display the graphic of today\'s heart rate compared to last days"))
        self.checkBox_3.setText(_translate("Choice_Heart", "Others informations"))
        self.label.setText(_translate("Choice_Heart", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Select what you want </span></p></body></html>"))
        self.pushButton.setText(_translate("Choice_Heart", "Ok !"))


    def handleButtonOk(self):

        choice = []

        choice.append(self.checkBox.isChecked())
        choice.append(self.checkBox_2.isChecked())
        choice.append(self.checkBox_3.isChecked())

        

