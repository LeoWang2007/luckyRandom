# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(862, 594)
        Form.setStyleSheet("/*background-color: rgb(187, 229, 255);*/")
        self.lab_number = QtWidgets.QLabel(Form)
        self.lab_number.setGeometry(QtCore.QRect(10, 80, 831, 291))
        font = QtGui.QFont()
        font.setFamily("Aa甜甜圈 (非商业使用)")
        font.setPointSize(140)
        self.lab_number.setFont(font)
        self.lab_number.setStyleSheet("color: rgb(91, 0, 183);")
        self.lab_number.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lab_number.setObjectName("lab_number")
        self.btn_play = QtWidgets.QPushButton(Form)
        self.btn_play.setGeometry(QtCore.QRect(340, 400, 141, 51))
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(22)
        self.btn_play.setFont(font)
        self.btn_play.setStyleSheet("QPushButton{border-radius:10px;background-color:rgb(58, 164, 221)}\n"
"QPushButton:hover{background-color:rgb(0, 196, 255)}\n"
"QPushButton:pressed{background-color: rgb(192, 242, 255);\n"
"}\n"
"\n"
"")
        self.btn_play.setObjectName("btn_play")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 861, 591))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("img/bgNew.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.btn_admin = QtWidgets.QPushButton(Form)
        self.btn_admin.setGeometry(QtCore.QRect(780, 560, 81, 31))
        self.btn_admin.setStyleSheet("QPushButton{border-radius:10px;background-color:rgb(58, 164, 221)}\n"
"QPushButton:hover{background-color:rgb(0, 196, 255)}\n"
"QPushButton:pressed{background-color: rgb(192, 242, 255);\n"
"}\n"
"\n"
"")
        self.btn_admin.setObjectName("btn_admin")
        self.label_2.raise_()
        self.btn_play.raise_()
        self.lab_number.raise_()
        self.btn_admin.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "WonderTools - 2020六一活动抽奖"))
        self.lab_number.setText(_translate("Form", ">_<"))
        self.btn_play.setText(_translate("Form", "抽奖"))
        self.btn_admin.setText(_translate("Form", "admin"))

