# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aisearch_gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(796, 700)
        self.e_nomor = QtWidgets.QLineEdit(Dialog)
        self.e_nomor.setGeometry(QtCore.QRect(120, 40, 151, 20))
        self.e_nomor.setObjectName("e_nomor")
        self.l_nama = QtWidgets.QLabel(Dialog)
        self.l_nama.setGeometry(QtCore.QRect(20, 70, 91, 16))
        self.l_nama.setObjectName("l_nama")
        self.b_search = QtWidgets.QPushButton(Dialog)
        self.b_search.setGeometry(QtCore.QRect(200, 150, 75, 23))
        self.b_search.setObjectName("b_search")
        self.l_nomor = QtWidgets.QLabel(Dialog)
        self.l_nomor.setGeometry(QtCore.QRect(20, 40, 91, 16))
        self.l_nomor.setObjectName("l_nomor")
        self.e_alamat = QtWidgets.QLineEdit(Dialog)
        self.e_alamat.setGeometry(QtCore.QRect(120, 110, 151, 20))
        self.e_alamat.setObjectName("e_alamat")
        self.l_copyright = QtWidgets.QLabel(Dialog)
        self.l_copyright.setGeometry(QtCore.QRect(300, 560, 211, 225))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.l_copyright.setFont(font)
        self.l_copyright.setObjectName("l_copyright")
        self.l_alamat = QtWidgets.QLabel(Dialog)
        self.l_alamat.setGeometry(QtCore.QRect(20, 110, 91, 16))
        self.l_alamat.setObjectName("l_alamat")
        self.e_nama = QtWidgets.QLineEdit(Dialog)
        self.e_nama.setGeometry(QtCore.QRect(120, 70, 151, 20))
        self.e_nama.setObjectName("e_nama")
        self.gp_view = QtWidgets.QGraphicsView(Dialog)
        self.gp_view.setGeometry(QtCore.QRect(300, 20, 481, 630))
        self.gp_view.setObjectName("gp_view")
        self.b_zoom_in = QtWidgets.QPushButton(Dialog)
        self.b_zoom_in.setGeometry(QtCore.QRect(570, 660, 75, 23))
        self.b_zoom_in.setObjectName("b_zoom_in")
        self.b_zoom_out = QtWidgets.QPushButton(Dialog)
        self.b_zoom_out.setGeometry(QtCore.QRect(700, 660, 75, 23))
        self.b_zoom_out.setObjectName("b_zoom_out")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "aiSearch"))
        self.l_nama.setText(_translate("Dialog", "Nama                : "))
        self.b_search.setText(_translate("Dialog", "Search"))
        self.l_nomor.setText(_translate("Dialog", "Nomor               : "))
        self.l_copyright.setText(_translate("Dialog", "?? 2020 Antesena Multidata Selaras"))
        self.l_alamat.setText(_translate("Dialog", "Kota/Kab/Prov  : "))
        self.b_zoom_in.setText(_translate("Dialog", "ZoomIn"))
        self.b_zoom_out.setText(_translate("Dialog", "ZoomOut"))

