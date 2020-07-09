# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 489)
        self.btn_toEdit = QtWidgets.QPushButton(Form)
        self.btn_toEdit.setGeometry(QtCore.QRect(10, 360, 211, 51))
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(13)
        self.btn_toEdit.setFont(font)
        self.btn_toEdit.setStyleSheet("QPushButton{border-radius:10px;background-color:rgb(58, 164, 221)}\n"
"QPushButton:hover{background-color:rgb(0, 196, 255)}\n"
"QPushButton:pressed{background-color: rgb(192, 242, 255);\n"
"}\n"
"\n"
"")
        self.btn_toEdit.setObjectName("btn_toEdit")
        self.btn_toIndex = QtWidgets.QPushButton(Form)
        self.btn_toIndex.setGeometry(QtCore.QRect(230, 360, 161, 51))
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(11)
        self.btn_toIndex.setFont(font)
        self.btn_toIndex.setStyleSheet("QPushButton{border-radius:10px;background-color:rgb(58, 164, 221)}\n"
"QPushButton:hover{background-color:rgb(0, 196, 255)}\n"
"QPushButton:pressed{background-color: rgb(192, 242, 255);\n"
"}\n"
"\n"
"")
        self.btn_toIndex.setObjectName("btn_toIndex")
        self.edit_numberEdit = QtWidgets.QTextEdit(Form)
        self.edit_numberEdit.setGeometry(QtCore.QRect(10, 10, 381, 301))
        self.edit_numberEdit.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"border: 1px solid ;\n"
"background-color: rgb(255, 255, 255);")
        self.edit_numberEdit.setReadOnly(False)
        self.edit_numberEdit.setObjectName("edit_numberEdit")
        self.btn_delAll = QtWidgets.QPushButton(Form)
        self.btn_delAll.setGeometry(QtCore.QRect(10, 420, 211, 51))
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(13)
        self.btn_delAll.setFont(font)
        self.btn_delAll.setStyleSheet("QPushButton{border-radius:10px;background-color:rgb(255, 137, 137)}\n"
"QPushButton:hover{background-color:rgb(255, 97, 97)}\n"
"QPushButton:pressed{background-color: rgb(255, 0, 0);\n"
"}\n"
"")
        self.btn_delAll.setObjectName("btn_delAll")
        self.nowLuckCnt = QtWidgets.QLineEdit(Form)
        self.nowLuckCnt.setGeometry(QtCore.QRect(120, 320, 121, 25))
        self.nowLuckCnt.setReadOnly(True)
        self.nowLuckCnt.setObjectName("nowLuckCnt")
        self.tip1 = QtWidgets.QLabel(Form)
        self.tip1.setGeometry(QtCore.QRect(10, 320, 111, 18))
        self.tip1.setObjectName("tip1")
        self.btn_closeProgram = QtWidgets.QPushButton(Form)
        self.btn_closeProgram.setGeometry(QtCore.QRect(230, 420, 161, 51))
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(13)
        self.btn_closeProgram.setFont(font)
        self.btn_closeProgram.setStyleSheet("QPushButton{border-radius:10px;background-color:rgb(255, 137, 137)}\n"
"QPushButton:hover{background-color:rgb(255, 97, 97)}\n"
"QPushButton:pressed{background-color: rgb(255, 0, 0);\n"
"}\n"
"")
        self.btn_closeProgram.setObjectName("btn_closeProgram")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "管理员管理窗口"))
        self.btn_toEdit.setToolTip(_translate("Form", "<html><head/><body><p>将程序内部数据同步至控制台</p></body></html>"))
        self.btn_toEdit.setText(_translate("Form", "内部数据同步显示"))
        self.btn_toIndex.setToolTip(_translate("Form", "<html><head/><body><p>将控制台数据同步至程序中</p></body></html>"))
        self.btn_toIndex.setText(_translate("Form", "输入数据执行"))
        self.edit_numberEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btn_delAll.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" color:#ff0000;\">请备份数据！！！</span></p><p>清空控制台数据及程序内部数据</p><p><span style=\" color:#ff0000;\">如需保留数据请在操作时备份数据</span></p></body></html>"))
        self.btn_delAll.setText(_translate("Form", "清空已抽奖数据"))
        self.tip1.setText(_translate("Form", "已抽取人数："))
        self.btn_closeProgram.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" color:#ff0000;\">用于管理员退出程序</span></p><p><span style=\" color:#ff0000;\">请谨慎操作</span></p></body></html>"))
        self.btn_closeProgram.setText(_translate("Form", "退出程序"))

