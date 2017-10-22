# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_image.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SamsungWindow(object):
    def setupUi(self, FitbitWindow):
        FitbitWindow.setObjectName("FitbitWindow")
        FitbitWindow.resize(291, 360)
        FitbitWindow.setMinimumSize(QtCore.QSize(291, 360))
        font = QtGui.QFont()
        font.setItalic(False)
        FitbitWindow.setFont(font)
        FitbitWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(FitbitWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnCoeur = QtWidgets.QPushButton(self.centralwidget)
        self.btnCoeur.setGeometry(QtCore.QRect(20, 20, 251, 181))
        self.btnCoeur.setStyleSheet("border-image: url(picture/coeur.jpg);\n"
"border-color: rgb(0, 0, 0);")
        self.btnCoeur.setText("")
        self.btnCoeur.setObjectName("btnCoeur")
        self.btnData = QtWidgets.QPushButton(self.centralwidget)
        self.btnData.setGeometry(QtCore.QRect(20, 210, 251, 101))
        self.btnData.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"font: 12pt \"Adobe Kaiti Std R\";")
        self.btnData.setObjectName("btnData")
        FitbitWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FitbitWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 291, 21))
        self.menubar.setObjectName("menubar")
        self.menuHome = QtWidgets.QMenu(self.menubar)
        self.menuHome.setObjectName("menuHome")
        FitbitWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FitbitWindow)
        self.statusbar.setObjectName("statusbar")
        FitbitWindow.setStatusBar(self.statusbar)
        self.actionExport = QtWidgets.QAction(FitbitWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionExit = QtWidgets.QAction(FitbitWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuHome.addAction(self.actionExit)
        self.menubar.addAction(self.menuHome.menuAction())

        self.retranslateUi(FitbitWindow)
        QtCore.QMetaObject.connectSlotsByName(FitbitWindow)

    def retranslateUi(self, FitbitWindow):
        _translate = QtCore.QCoreApplication.translate
        FitbitWindow.setWindowTitle(_translate("FitbitWindow", "MainWindow"))
        self.btnData.setText(_translate("FitbitWindow", "DATA EXPORT"))
        self.menuHome.setTitle(_translate("FitbitWindow", "Home"))
        self.actionExport.setText(_translate("FitbitWindow", "Export "))
        self.actionExit.setText(_translate("FitbitWindow", "Exit"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FitbitWindow = QtWidgets.QMainWindow()
    ui = Ui_SamsungWindow()
    ui.setupUi(FitbitWindow)
    FitbitWindow.show()
    sys.exit(app.exec_())

