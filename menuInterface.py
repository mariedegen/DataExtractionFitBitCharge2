# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.resize(464, 263)
        self.label = QtWidgets.QLabel(Menu)
        self.label.setGeometry(QtCore.QRect(70, 30, 301, 31))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Menu)
        self.pushButton.setGeometry(QtCore.QRect(30, 80, 171, 131))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("border-image: url(picture/fitbitCharge.png);\n"
"border-color: rgb(0, 0, 0);")
        self.pushButton_2 = QtWidgets.QPushButton(Menu)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 80, 171, 131))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("border-image: url(picture/samsungGear.jpg);\n"
"border-color: rgb(0, 0, 0);")
        self.label_2 = QtWidgets.QLabel(Menu)
        self.label_2.setGeometry(QtCore.QRect(80, 230, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Menu)
        self.label_3.setGeometry(QtCore.QRect(300, 230, 101, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Dialog"))
        self.label.setText(_translate("Menu", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Click on your device</span></p></body></html>"))
        self.label_2.setText(_translate("Menu", "Fitbit Charge 2"))
        self.label_3.setText(_translate("Menu", "Samung Gear Fit 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Menu = QtWidgets.QDialog()
    ui = Ui_Menu()
    ui.setupUi(Menu)
    Menu.show()
    sys.exit(app.exec_())


