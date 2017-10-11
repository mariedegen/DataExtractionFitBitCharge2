#!/usr/bin/python
 
from PyQt5 import QtGui, QtCore, QtWidgets
import sys


import interface
 
class ImageViewer(QtWidgets.QMainWindow, interface.Ui_FitbitWindow):
    def __init__(self, parent=None):
        super(ImageViewer, self).__init__(parent)
        self.setupUi(self)

        self.TEST_GRAPHIC.installEventFilter(self)
        

    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.MouseButtonPress and source == self.TEST_GRAPHIC):
            if event.button() == QtCore.Qt.LeftButton:
                print("Press!")
        return True;
 
    def main(self):
        self.show()

def mainInterface(): 
#if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    imageViewer = ImageViewer()
    imageViewer.main()
    app.exec_()
