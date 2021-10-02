import threading
import time
from typing import Text
import numpy as np
import pyscreenshot as ImageGrab
import cv2
from tkinter import *
import os
import pytesseract
from PIL import Image
import pyautogui
import eel
import pyowm
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
import multiprocessing
import palette


class Ui_Form(object):
    def setupUi(self, Form):
        title = QtWidgets.QLabel(Form)
        title.move(80, 130)
        title.adjustSize()
        Form.setWindowTitle("Accepter")
        Form.setFixedSize(260, 350)
        Form.setGeometry(700, 500, 330, 400)
        title = QtWidgets.QLabel(Form)
        title.move(80, 130)
        title.adjustSize()
        Form.setObjectName("Form")
        Form.resize(271, 309)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        Form.setFont(font)
        Form.setWindowIcon(QtGui.QIcon("D:/PM/AAMM/Icon.jpg"))
        Form.setStyleSheet("QWidget{\n"
"    background-image: url('D:/PM/AAMM/5feb5a04d15d7_cover.png');\n"
"}\n"
"QPushButton {\n"   
"    background: #f2eded;\n"
"    font-size:15px;\n"
"    cursor: pointer;\n"
"    opacity: 0.7s;\n"
"    border: 0px;\n"
"    opacity: 0.7s;\n"
"    font-family:Arial"
"}\n"
"QPushButton:hover{\n"   
"    opacity: 2s;\n"
"    background: silver;"
"}\n"
"QLineEdit{\n"
"    font-size:15px;\n"
"    color:#e3e1e1;\n"
"    text-align:right;\n"
"    font-family:Arial\n"
"}\n"
"QLabel{\n"
"    color:#e3e1e1;\n"
"    text-align:right;\n"
"    font-size:18px;\n"
"    font-family:Arial\n"
"}\n"
"")         
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(70, 170, 131, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 230, 131, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(40, 90, 181, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 60, 150, 21))
        self.label.setObjectName("label")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Accepter"))
        self.pushButton.setText(_translate("Form", "START"))
        self.pushButton_2.setText(_translate("Form", "STOP"))
        self.label.setText(_translate("Form", "Word accept (eng)"))
        self.pushButton.clicked.connect(self.on_click)
        self.works = MainQthread(funct = self.work, v = self.lineEdit)
        self.pushButton_2.clicked.connect(lambda: self.on_clickStop())

    def on_click(self):
        print()
        self.works.start()

    def on_clickStop(self):
        print()
        print(self.works.terminate())

    def work(self, v):
        while True:
            pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
            picture = 'D:\PM\AAMM\screenshot.png'
            last_time = time.time()
            screen = np.array(ImageGrab.grab(bbox=(599, 261, 1316, 565)))
            # print('loop took {} seconds'.format(time.time()-last_time))
            last_time = time.time()
            # cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
            cv2.imwrite(picture, screen)
            img = cv2.imread('D:\PM\AAMM\screenshot.png')
            text = pytesseract.image_to_string(img)
            serch = text.find(v.text())
            if serch == -1:
                print(serch)
            else:
                pyautogui.moveTo(942, 429)
                pyautogui.click()
                break



class MainQthread(QThread):
    def __init__(self, funct, v, parent=None):
        super().__init__()
        self.funct = funct
        self.v = v

    def run(self):
        self.funct(self.v)


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    Form.setWindowIcon(QtGui.QIcon("D:/PM/AAMM/Icon.jpg"))
    Form.setWindowTitle("Accepter")
    Form.setFixedSize(263, 350)
    Form.setGeometry(700, 500, 270, 360)
    sys.exit(app.exec_())

    
if __name__ == "__main__":
    main()

