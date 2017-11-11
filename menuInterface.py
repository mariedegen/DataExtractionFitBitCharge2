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
        self.label.setGeometry(QtCore.QRect(70, 40, 301, 31))
        self.label.setStyleSheet("font: 8pt \"OCR A Std\";\n"
"background-color: rgb(255, 255, 127);\n"
"")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Menu)
        self.pushButton.setGeometry(QtCore.QRect(30, 80, 171, 131))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("border-image: url(picture/fitbitCharge.png);\n"
"border-color: rgb(0, 0, 0);")
        self.pushButton_2 = QtWidgets.QPushButton(Menu)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 80, 171, 131))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("border-image: url(picture/samsungGear.png);\n"
"border-color: rgb(0, 0, 0);")
        self.label_2 = QtWidgets.QLabel(Menu)
        self.label_2.setGeometry(QtCore.QRect(50, 230, 131, 16))
        self.label_2.setStyleSheet("font: 8pt \"OCR A Std\";\n"
"background-color: rgb(255, 170, 127);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Menu)
        self.label_3.setGeometry(QtCore.QRect(270, 230, 141, 20))
        self.label_3.setStyleSheet("font: 8pt \"OCR A Std\";\n"
"background-color: rgb(170, 170, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Menu)
        self.label_4.setGeometry(QtCore.QRect(26, 10, 411, 31))
        self.label_4.setStyleSheet("font: 8pt \"OCR A Std\";\n"
"background-color: rgbrgb(85, 255, 127);")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Dialog"))
        self.label.setText(_translate("Menu", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Click on your device</span></p></body></html>"))
        self.label_2.setText(_translate("Menu", "Fitbit Charge 2"))
        self.label_3.setText(_translate("Menu", "Samung Gear Fit 2"))
        self.label_4.setText(_translate("Menu", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">MENU</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Menu = QtWidgets.QDialog()
    ui = Ui_Menu()
    ui.setupUi(Menu)
    Menu.show()
    sys.exit(app.exec_())

