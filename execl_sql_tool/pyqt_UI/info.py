# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_info_Dialog(object):
    def setupUi(self, info_Dialog):
        info_Dialog.setObjectName("info_Dialog")
        info_Dialog.resize(254, 165)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        info_Dialog.setFont(font)
        self.label = QtWidgets.QLabel(info_Dialog)
        self.label.setGeometry(QtCore.QRect(30, 90, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(info_Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 201, 61))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(info_Dialog)
        self.pushButton.setGeometry(QtCore.QRect(90, 120, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(info_Dialog)
        self.pushButton.clicked.connect(info_Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(info_Dialog)

    def retranslateUi(self, info_Dialog):
        _translate = QtCore.QCoreApplication.translate
        info_Dialog.setWindowTitle(_translate("info_Dialog", "软件信息"))
        self.label.setText(_translate("info_Dialog", "version:1.0"))
        self.label_2.setText(_translate("info_Dialog", "软件介绍：本软件主要作用\n"
"是通过execl和mysql进行数\n"
"据互相转存"))
        self.pushButton.setText(_translate("info_Dialog", "关闭"))

