import sys
import random
import time
import threading
import json
# import pygame

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtMultimedia
from PyQt5.QtCore import QUrl

import window
import admin


canClose = False
class NewWidget(QWidget):#防退出窗口
    def closeEvent(self, event):
        global canClose
        if canClose == False:
            QMessageBox.warning(mainwindow, "禁止退出", "请授权后在[管理员管理界面]中退出程序", QMessageBox.Yes)
            event.ignore()
        else:
            event.accept()

app = QApplication(sys.argv)
mainwindow = NewWidget()
ui = window.Ui_Form()
ui.setupUi(mainwindow)
# mainwindow.setWindowFlags(Qt.FramelessWindowHint)

adminwindow = QWidget()
adminwin = admin.Ui_Form()
adminwin.setupUi(adminwindow)

IsRun = False# 标记抽奖是否正在滚动
visited = []# 已抽奖的学号

def windowDo():
    ui.btn_admin.clicked.connect(btn_admin_func)
    ui.btn_play.clicked.connect(btn_play_func)
    ui.btn_admin.setShortcut('ctrl+shift+a')# admin按钮快捷键
    ui.btn_play.setShortcut('l')# 抽奖按钮快捷键
    adminwin.btn_toEdit.clicked.connect(toEdit)
    adminwin.btn_delAll.clicked.connect(delAll)
    adminwin.btn_toIndex.clicked.connect(toIndex)
    adminwin.btn_closeProgram.clicked.connect(btn_closeProgram_func)

def btn_admin_func():
    text, ok = QInputDialog.getText(mainwindow, '需要密码授权', '管理员操作需[密码]授权，请输入密码', QLineEdit.Password)# 密码输入框
    # text, okPressed = QInputDialog.getText(adminwindow, "需要密码授权","管理员操作需[密码]授权，请输入密码", QLineEdit.Normal, "")# 普通输入框
    if text == "12345678":
        adminwindow.show()
        adminwin.edit_numberEdit.setText(str(visited))  # 更新显示数据
        adminwin.nowLuckCnt.setText(str(len(visited)))  # 显示已抽取人数
    else:
        QMessageBox.critical(mainwindow, "密码错误","需要[正确密码]访问管理员页面",QMessageBox.Yes,QMessageBox.Yes)

def btn_play_func():
    global IsRun
    global visited


    # 已全部抽取
    if len(visited) == 46:
        QMessageBox.information(mainwindow, "均已抽取", "所有学号均已抽取 请前往管理页面清空数据", QMessageBox.Yes)

    if IsRun:
        IsRun = False
    else:
        IsRun = True
        threading.Thread(target=randomPlay).start()

def btn_closeProgram_func():
    if QMessageBox.warning(adminwindow, "关闭程序确认", "执行本操作将[退出程序]", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes) == QMessageBox.Yes:
        exit(0)

def randomPlay():# 抽奖程序主函数
    global visited
    global IsRun


    # 生成原定学号
    nowRand = random.randint(1, 45)# 设置第一次比较值

    if len(visited) == 7:
        nowRand = 46

    while nowRand in visited:# 防止学号重复
        nowRand = random.randint(1, 45)
    visited.append(nowRand)# 已抽取学号加入队列

    # 彩蛋：抽取童老师
    if nowRand == 46:
        nowRand = "童"

    # print(len(visited))
    # print(visited)

    while IsRun:# 开始假滚动
        ui.lab_number.setText(str(random.randint(1, 45)))
        time.sleep(0.1)
    ui.lab_number.setText(str(nowRand))# 切回原定随机数

# 管理员操作
def toIndex():
    global visited
    try:
        visited = json.loads(adminwin.edit_numberEdit.toPlainText())
    except:
        QMessageBox.information(adminwindow, "错误", "输入数据不合法", QMessageBox.Yes)
    # print(visited)
def toEdit():
    global visited
    adminwin.edit_numberEdit.setText(str(visited))# 更新显示数据

    adminwin.nowLuckCnt.setText(str(len(visited)))# 显示已抽取人数
def delAll():
    global visited
    if QMessageBox.warning(adminwindow, "清空名单再次确认", "[请备份]\n是否要执行[清空已抽奖名单]操作，此操作不可逆", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes) == QMessageBox.Yes:
        visited = []# 清空名单
        adminwin.edit_numberEdit.setText(str(visited))# 更新显示数据

    adminwin.nowLuckCnt.setText(str(len(visited)))  # 显示已抽取人数

windowDo()# 执行窗口初始化操作
mainwindow.show()
sys.exit(app.exec_())