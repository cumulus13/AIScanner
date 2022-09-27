# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aisearch_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(796, 700)
        self.e_nomor = QtWidgets.QLineEdit(Dialog)
        self.e_nomor.setGeometry(QtCore.QRect(120, 40, 171, 20))
        self.e_nomor.setObjectName("e_nomor")
        self.l_nama = QtWidgets.QLabel(Dialog)
        self.l_nama.setGeometry(QtCore.QRect(20, 70, 91, 16))
        self.l_nama.setObjectName("l_nama")
        self.b_search = QtWidgets.QPushButton(Dialog)
        self.b_search.setGeometry(QtCore.QRect(200, 230, 75, 23))
        self.b_search.setObjectName("b_search")
        self.l_nomor = QtWidgets.QLabel(Dialog)
        self.l_nomor.setGeometry(QtCore.QRect(20, 40, 91, 16))
        self.l_nomor.setObjectName("l_nomor")
        self.e_alamat = QtWidgets.QLineEdit(Dialog)
        self.e_alamat.setGeometry(QtCore.QRect(120, 110, 171, 20))
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
        self.e_nama.setGeometry(QtCore.QRect(120, 70, 171, 20))
        self.e_nama.setObjectName("e_nama")
        self.gp_view = QtWidgets.QGraphicsView(Dialog)
        self.gp_view.setGeometry(QtCore.QRect(300, 20, 481, 581))
        self.gp_view.setObjectName("gp_view")
        self.b_zoom_in = QtWidgets.QPushButton(Dialog)
        self.b_zoom_in.setGeometry(QtCore.QRect(570, 660, 75, 23))
        self.b_zoom_in.setObjectName("b_zoom_in")
        self.b_zoom_out = QtWidgets.QPushButton(Dialog)
        self.b_zoom_out.setGeometry(QtCore.QRect(700, 660, 75, 23))
        self.b_zoom_out.setObjectName("b_zoom_out")
        self.b_print = QtWidgets.QPushButton(Dialog)
        self.b_print.setGeometry(QtCore.QRect(200, 330, 75, 23))
        self.b_print.setObjectName("b_print")
        self.b_scan = QtWidgets.QPushButton(Dialog)
        self.b_scan.setGeometry(QtCore.QRect(200, 270, 75, 23))
        self.b_scan.setObjectName("b_scan")
        self.b_save = QtWidgets.QPushButton(Dialog)
        self.b_save.setGeometry(QtCore.QRect(200, 300, 75, 23))
        self.b_save.setObjectName("b_save")
        self.l_na = QtWidgets.QLabel(Dialog)
        self.l_na.setGeometry(QtCore.QRect(310, 620, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.l_na.setFont(font)
        self.l_na.setText("")
        self.l_na.setScaledContents(True)
        self.l_na.setAlignment(QtCore.Qt.AlignCenter)
        self.l_na.setWordWrap(True)
        self.l_na.setObjectName("l_na")
        self.l_na_l = QtWidgets.QLabel(Dialog)
        self.l_na_l.setGeometry(QtCore.QRect(20, 150, 91, 16))
        self.l_na_l.setObjectName("l_na_l")
        self.e_na = QtWidgets.QLineEdit(Dialog)
        self.e_na.setGeometry(QtCore.QRect(120, 150, 171, 20))
        self.e_na.setObjectName("e_na")
        self.e_keyword = QtWidgets.QLineEdit(Dialog)
        self.e_keyword.setGeometry(QtCore.QRect(120, 190, 171, 20))
        self.e_keyword.setObjectName("e_keyword")
        self.l_keyword = QtWidgets.QLabel(Dialog)
        self.l_keyword.setGeometry(QtCore.QRect(20, 190, 91, 16))
        self.l_keyword.setObjectName("l_keyword")
        self.l_qrcode = QtWidgets.QLabel(Dialog)
        self.l_qrcode.setGeometry(QtCore.QRect(80, 370, 141, 141))
        self.l_qrcode.setAlignment(QtCore.Qt.AlignCenter)
        self.l_qrcode.setObjectName("l_qrcode")
        self.l_barcode = QtWidgets.QLabel(Dialog)
        self.l_barcode.setGeometry(QtCore.QRect(30, 540, 241, 51))
        self.l_barcode.setAlignment(QtCore.Qt.AlignCenter)
        self.l_barcode.setObjectName("l_barcode")
        self.l_na2 = QtWidgets.QLabel(Dialog)
        self.l_na2.setGeometry(QtCore.QRect(30, 600, 241, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(6)
        self.l_na2.setFont(font)
        self.l_na2.setAlignment(QtCore.Qt.AlignCenter)
        self.l_na2.setObjectName("l_na2")
        self.c_jenis = QtWidgets.QComboBox(Dialog)
        self.c_jenis.setGeometry(QtCore.QRect(20, 230, 161, 22))
        self.c_jenis.setCurrentText("")
        self.c_jenis.setObjectName("c_jenis")
        self.hs_dpi = QtWidgets.QSlider(Dialog)
        self.hs_dpi.setGeometry(QtCore.QRect(20, 270, 161, 22))
        self.hs_dpi.setOrientation(QtCore.Qt.Horizontal)
        self.hs_dpi.setObjectName("hs_dpi")
        self.l_dpi = QtWidgets.QLabel(Dialog)
        self.l_dpi.setGeometry(QtCore.QRect(60, 290, 91, 20))
        self.l_dpi.setAlignment(QtCore.Qt.AlignCenter)
        self.l_dpi.setObjectName("l_dpi")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "aiSearch"))
        self.l_nama.setText(_translate("Dialog", "Nama                : "))
        self.b_search.setText(_translate("Dialog", "Search"))
        self.l_nomor.setText(_translate("Dialog", "Nomor               : "))
        self.l_copyright.setText(_translate("Dialog", "© 2020 Antesena Multidata Selaras"))
        self.l_alamat.setText(_translate("Dialog", "Kota/Kab/Prov  : "))
        self.b_zoom_in.setText(_translate("Dialog", "ZoomIn"))
        self.b_zoom_out.setText(_translate("Dialog", "ZoomOut"))
        self.b_print.setText(_translate("Dialog", "Print"))
        self.b_scan.setText(_translate("Dialog", "Scan"))
        self.b_save.setText(_translate("Dialog", "Save"))
        self.l_na_l.setText(_translate("Dialog", "Nomor Arsip      :"))
        self.l_keyword.setText(_translate("Dialog", "Keyword           :"))
        self.l_qrcode.setText(_translate("Dialog", "qrcode"))
        self.l_barcode.setText(_translate("Dialog", "barcode"))
        self.l_na2.setText(_translate("Dialog", "nomor arsip"))
        self.l_dpi.setText(_translate("Dialog", "DPI"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
