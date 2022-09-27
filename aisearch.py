import os
import sys
#from pydebugger.debug import debug
from aisearch_gui import *
from PyQt5.QtWidgets import QApplication, QDialog, QSlider
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import *
from barcode.writer import ImageWriter
from barcode import Code39
import pyqrcode
from pydebugger.debug import debug
#from pyzbar.pyzbar import decode
#from PIL import Image
import aiScanner

class My_Application(QDialog):
    def __init__(self):
        super().__init__()
        #super(My_Application, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.b_search.clicked.connect(self.checkPath)
        self.ui.b_zoom_in.clicked.connect(self.zoomIn)
        self.ui.b_zoom_out.clicked.connect(self.zoomOut)
        self.current_scale = 0.6
        self.dbname = 'aidb.db'
        self.aiscanner = aiScanner.aiScanner()
        
        self.ui.l_qrcode.setText('')
        self.ui.l_barcode.setText('')
        self.ui.l_na2.setText('')
        
        self.nama = self.ui.e_nama.text()
        self.nomor = self.ui.e_nomor.text()
        self.region = self.ui.e_alamat.text()
        self.isi = self.ui.e_keyword.text()
        
        self.image = ''
        
        self.data = ''
        self.na = self.ui.e_na.text()
        self.barcode = os.path.join(os.path.dirname(__file__), 'images', 'barcode')
        self.qrcode = os.path.join(os.path.dirname(__file__), 'images', 'qrcode')
        
        if not os.path.isdir(self.barcode):
            os.makedirs(self.barcode)
        if not os.path.isdir(self.qrcode):
            os.makedirs(self.qrcode)
            
        self.additem_combo()
        
        #self.ui.hs_dpi.setTickPosition(QSlider.TicksBelow)
        #self.ui.hs_dpi.setTickInterval(5)
        self.dpi = 70
        self.ui.hs_dpi.setMaximum(2400)
        self.ui.hs_dpi.setValue(self.dpi)
        self.ui.l_dpi.setText("{0} DPI".format(self.dpi))
        self.ui.hs_dpi.valueChanged.connect(self.slider_changer)
        
        self.ui.b_scan.clicked.connect(self.scanning)
        
    def scanning(self):
        jenis, nums, alamat, number, isi, image = self.aiscanner.scanning(dpi = self.dpi, quiet = True)
        data = [['', jenis, nums, alamat, number, isi, image]]
        #print("data =", data)
        self.set_data(data)
        
        image_path = self.image
        
        
        if os.path.isfile(image_path):
            scene = QtWidgets.QGraphicsScene(self)
            pixmap = QPixmap(image_path)
            pixmap.scaledToWidth(2)
            #pixmap.scaled(64, 64, QtCore.Qt.KeepAspectRatio)
            #pixmap.scaled(1, 1, Qt.KeepAspectRatio, transformMode = Qt.SmoothTransformation)
            item = QtWidgets.QGraphicsPixmapItem(pixmap)
            item.setScale(self.current_scale)
            scene.addItem(item)
            self.ui.gp_view.setScene(scene)
        
        if self.na:
            barcode_img = QPixmap(self.create_barcode(self.na))
            qrcode_img = QPixmap(self.create_qrcode(self.na))
            
            self.ui.l_barcode.setPixmap(barcode_img)
            self.ui.l_qrcode.setPixmap(qrcode_img)        
        
        
    def slider_changer(self):
        self.dpi = self.ui.hs_dpi.value()
        self.ui.l_dpi.setText("{0} DPI".format(self.dpi))
            
    def additem_combo(self):
        mail = QIcon(os.path.join(os.path.dirname(__file__), 'icons', 'mail.png'))
        image = QIcon(os.path.join(os.path.dirname(__file__), 'icons', 'image.png'))
        camera = QIcon(os.path.join(os.path.dirname(__file__), 'icons', 'camera.png'))
        self.ui.c_jenis.addItem(mail, 'Surat')
        self.ui.c_jenis.addItem(image, 'Gambar')
        self.ui.c_jenis.addItem(camera, 'Video')
        #self.ui.c_jenis.setCurrentIndex(0)
        
    def create_barcode(self, data):
        barcode = Code39(data, writer = ImageWriter())
        name = data.replace("/", "_")
        save = os.path.join(self.barcode, name)
        debug(save = save, debug = True)
        barcode.save(save) + ".png"
        return save + ".png"
    
    def create_qrcode(self, data):
        c = pyqrcode.create(data)
        name = data.replace("/", "_")
        save = os.path.join(self.barcode, name)# + ".png"
        debug(save_qrcode = save, debug = True)
        c.png(save, scale = 3)
        return save
        
    def decode_data(self, data):
        if sys.version_info.major == 3:
            if isinstance(data, str):
                data = bytes(data.encode('utf-8'))
        return base64.b64decode(data)
        
    def get_data(self):
    #def get_data(self, na = '', nama = '', nomor = '', region = ''):
        import sqlite3
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        #if self.na:
            #SQL = "SELECT * FROM arsip WHERE na like '%{0}%';".format(self.na)
        #else:
        SQL = "SELECT * FROM arsip WHERE nama like '%{0}%' and nomor like '%{1}%' and region like '%{2}%' and isi like '%{3}%';".format(self.nama, self.nomor, self.region, self.isi)
        print("SQL =", SQL)
        cur.execute(SQL)
        conn.commit()
        data = cur.fetchall()
        print("data =", data)
        self.data = data
        return data
    
    def set_data(self, data = None):
        if not data:
            data = self.data
        self.ui.e_nama.setText(data[0][1])
        self.ui.e_nomor.setText(data[0][2])
        self.ui.e_alamat.setText(data[0][3])
        self.ui.l_na.setText(data[0][4])
        self.ui.e_na.setText(data[0][4])
        #self.ui.e_keyword.setText(data[0][5])
        self.image = data[0][6]
        self.na = self.ui.e_na.text()
        self.ui.l_na2.setText(data[0][4])
        
        
    def zoomIn(self):
        self.current_scale += 0.1
        self.checkPath()
        
    def zoomOut(self):
        self.current_scale -= 0.1
        self.checkPath()

    def checkPath(self):
        #image_path = self.ui.lineEdit.text()
        self.nama = self.ui.e_nama.text()
        self.nomor = self.ui.e_nomor.text()
        self.region = self.ui.e_alamat.text()
        self.image = ''
        self.isi = self.ui.e_keyword.text()
        
        self.get_data()
        self.set_data()
        
        image_path = self.image
        
        
        if os.path.isfile(image_path):
            scene = QtWidgets.QGraphicsScene(self)
            pixmap = QPixmap(image_path)
            pixmap.scaledToWidth(2)
            #pixmap.scaled(64, 64, QtCore.Qt.KeepAspectRatio)
            #pixmap.scaled(1, 1, Qt.KeepAspectRatio, transformMode = Qt.SmoothTransformation)
            item = QtWidgets.QGraphicsPixmapItem(pixmap)
            item.setScale(self.current_scale)
            scene.addItem(item)
            self.ui.gp_view.setScene(scene)
        
        if self.na:
            barcode_img = QPixmap(self.create_barcode(self.na))
            qrcode_img = QPixmap(self.create_qrcode(self.na))
            
            self.ui.l_barcode.setPixmap(barcode_img)
            self.ui.l_qrcode.setPixmap(qrcode_img)
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    class_instance = My_Application()
    class_instance.show()
    sys.exit(app.exec_())

    #c = My_Application()
    #c.get_data("KETERANGAN DOMISI", "212/SKD/VII/2017", "KABUPATEN KULON PROGO")
    #c.get_data("C2254/ay362/XVE628/899/485/645/299/775/449/313/20200707233306")