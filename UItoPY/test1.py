# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from numpy.random import randint
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp,QMessageBox
from PyQt5.QtCore import Qt, QEvent, QObject

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 270, 201, 71))
        self.pushButton.setObjectName("pushButton")
        self.dial = QtWidgets.QDial(self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(90, 260, 131, 111))
        self.dial.setObjectName("dial")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(60, 60, 211, 141))
        self.lcdNumber.setObjectName("lcdNumber")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 460, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 460, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 460, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        self.dial.valueChanged['int'].connect(self.lcdNumber.display)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "石头"))
        self.pushButton_3.setText(_translate("MainWindow", "剪刀"))
        self.pushButton_4.setText(_translate("MainWindow", "布"))

class MyMainWindow(QMainWindow, Ui_MainWindow):
        def __init__(self, parent=None):
            super(MyMainWindow, self).__init__(parent)
            self.setupUi(self)
            self.pushButton_2.clicked.connect(self.buttonclicked)  # here is where the issue is occurs
            self.pushButton_3.clicked.connect(self.buttonclicked)  # here is where the issue is occurs
            self.pushButton_4.clicked.connect(self.buttonclicked)  # here is where the issue is occurs

        def eventFilter(self, obj, event):
            if event.type() == QEvent.KeyPress:
                if event.key() == Qt.Key_Escape:
                    self.close()
            return super(MyMainWindow, self).eventFilter(obj, event)

        def buttonclicked(self):
            computer = randint(1, 3)
            player = 0
            sender = self.sender()
            if sender.text() == '剪刀':
                player = 1
            elif sender.text() == '石头':
                player = 2
            else:
                player = 3

            if player == computer:
                QMessageBox.about(self, '结果', '平手')
            elif player == 1 and computer == 2:
                QMessageBox.about(self, '结果', '电脑：石头，电脑赢了！')
            elif player == 2 and computer == 3:
                QMessageBox.about(self, '结果', '电脑：布，电脑赢了！')
            elif player == 3 and computer == 1:
                QMessageBox.about(self, '结果', '电脑：剪刀，电脑赢了！')
            elif computer == 1 and player == 2:
                QMessageBox.about(self, '结果', '电脑：剪刀，玩家赢了！')
            elif computer == 2 and player == 3:
                QMessageBox.about(self, '结果', '电脑：石头，玩家赢了！')
            elif computer == 3 and player == 1:
                QMessageBox.about(self, '结果', '电脑：布，玩家赢了！')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())