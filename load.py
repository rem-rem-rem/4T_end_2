from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import os

os.system("pyuic5 -x load.ui -o LOGIN.py ")

from LOGIN import *

class LOGIN_Main(Ui_MainWindow, QMainWindow):
    show_mode = False
    def __init__(self, mainwindow):
        QMainWindow.__init__(self)
        self.setupUi(mainwindow)
        mainwindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        mainwindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.close_button.clicked.connect(lambda: self.close())
        # self.setWindowTitle("rem")
        self.BoxButton.clicked.connect(lambda: self.BoxButtonn())
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.eye.clicked.connect(lambda: self.eye_click())
        
        self.close_button.clicked.connect(lambda: self.close())
        # self.setCentralWidget(self.close_button)
        self.EnterButton.clicked.connect(lambda: self.scan_password())
        self.comboboxx()

    def comboboxx(self):
        self.comboBox.currentTextChanged.connect(self.laygiatri)

    def  laygiatri(self):
        self.User.setText(self.comboBox.currentText())

    def close(self):
        sys.exit()

    def BoxButtonn(self):
        self.comboBox.showPopup()

    def scan_password(self):
        User_scan = self.User.text()
        Password_scan = self.Password.text()
    
    def eye_click(self):
        if self.show_mode == False:
            self.show_mode = True
            self.Password.setEchoMode(QtWidgets.QLineEdit.Normal)

        else :
            self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
            self.show_mode = False