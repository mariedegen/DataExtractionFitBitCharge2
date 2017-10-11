# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_image.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FitbitWindow(object):
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
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 130, 101, 111))
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("calorie.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 210, 101, 101))
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("etages.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 71, 71))
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("homme_qui_court.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 210, 31, 31))
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("minute.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QtCore.QRect(170, 20, 101, 101))
        self.label_6.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("localisation.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setWordWrap(False)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(100, 130, 61, 71))
        self.label_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("pas.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(130, 250, 141, 61))
        self.label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.label_8.setObjectName("label_8")
                
        self.TEST_GRAPHIC = QtWidgets.QGraphicsView(self.centralwidget)
        self.TEST_GRAPHIC.setGeometry(QtCore.QRect(20, 20, 141, 101))
        self.TEST_GRAPHIC.setMouseTracking(True)
        self.TEST_GRAPHIC.setStyleSheet("\n"
"border-image: url(coeur.jpg);")        
        self.TEST_GRAPHIC.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TEST_GRAPHIC.setLineWidth(2)
        self.TEST_GRAPHIC.setMidLineWidth(1)
        self.TEST_GRAPHIC.setObjectName("TEST_GRAPHIC")
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
        self.label_8.setText(_translate("FitbitWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Data export</span></p></body></html>"))
        self.TEST_GRAPHIC.setToolTip(_translate("FitbitWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.TEST_GRAPHIC.setWhatsThis(_translate("FitbitWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/Desktop/ProjetDI4/Fitbit/Nouvelle_app/coeur.jpg\" /></p></body></html>"))
        self.menuHome.setTitle(_translate("FitbitWindow", "Home"))
        self.actionExport.setText(_translate("FitbitWindow", "Export "))
        self.actionExit.setText(_translate("FitbitWindow", "Exit"))


    """def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.MouseButtonPress):
            if event.button() == QtCore.Qt.LeftButton:
                print("Press!")
        return super(Window, self).eventFilter(source, event)"""

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FitbitWindow = QtWidgets.QMainWindow()
    ui = Ui_FitbitWindow()
    ui.setupUi(FitbitWindow)
    FitbitWindow.show()
    sys.exit(app.exec_())

