#~*~*encode:utf-8*~*~
#~*~*encoding:utf-8*~*~
from __future__ import print_function
import win32api, win32con, win32gui, win32ui
import os
import sys
import re
import cv2
import numpy as np
import clipboard
from make_colors import make_colors
from pydebugger.debug import debug
import subprocess
import multiprocessing
from multiprocessing import Queue
import sqlite3
from datetime import datetime
import random
from configset import configset
if sys.version_info.major == 3:
    raw_input = input
import base64

class aiScanner(object):
    def __init__(self, image=None, configname = os.path.join(os.path.dirname(__file__), 'aiscanner.ini')):
        super(aiScanner, self)
        self.image = image
        self.configname = configname
        self.config = configset(self.configname)
        self.APP = self.config.get_config('tesseract', 'path', r"c:\SDK\Tesseract-OCR\tesseract.exe")
        self.dbname = self.config.get_config('database', 'name', 'aidb.db')
        self.conn = sqlite3.connect(self.dbname)
        self.cur = self.conn.cursor()
        self.now = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
        
    def encode_data(self, data):
        if sys.version_info.major == 3:
            if isinstance(data, str):
                data = bytes(data.encode('utf-8'))
        if sys.version_info.major == 3:
            return base64.b64encode(data).decode('utf-8')
        return base64.b64encode(data)
    
    def insert_db(self, data):
        SQL_CREATE = "CREATE TABLE IF NOT EXISTS arsip (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nama VARCHAR(255) NOT NULL, nomor VARCHAR(255) NOT NULL, region VARCHAR(255), na VARCHAR(255) NOT NULL, isi BLOB NOT NULL, file VARCHAR(255) NOT NULL);"
        SQL_INSERT = "INSERT INTO arsip (nama, nomor, region, na, isi, file) values ('{0}','{1}','{2}','{3}','{4}','{5}');".format(data[0], data[1], data[2], data[3], data[4], data[5])
        print("SQL_INSERT =", SQL_INSERT)
        self.cur.execute(SQL_CREATE)
        self.conn.commit()
        self.cur.execute(SQL_INSERT)
        self.conn.commit()

    def file_browser(self):
        select_dlg = win32ui.CreateFileDialog(1, ".jpg", "File hasil Scanning", win32con.OFN_OVERWRITEPROMPT, "Scanned file (*.jpg)|*.jpg|(*.png)|*.png|(*.jpeg)|*.jpeg|(*.tiff)|*.tiff|(*.bmp)|*.bmp|All Files (*.*)|*.*|")
        select_dlg.DoModal()
        selected_file = select_dlg.GetPathName()
        return selected_file
    
    def executeCommand(self, exeArgs, output):
        commandProcess = subprocess.Popen(exeArgs.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = commandProcess.communicate()
    
        output.put(out)
        
    def run(self, command):
        output = Queue()
        p = multiprocessing.Process(target=self.executeCommand, args=(command, output))
        if sys.version_info.major == 2:
            p.start()
            p.join()
        else:
            p.run()
            #p.join()
        #print output.get()    

    def scanning(self, image=None, dpi = 70, quiet = False):
        if not image:
            image = self.image
        if not image:
            image = self.file_browser()
        self.image = os.path.abspath(image)
        image_name = os.path.splitext(os.path.basename(image))[0]
        image = os.path.abspath(image)
        if not os.path.isfile(image):
            print(make_colors("Invalid Image File !", 'lw' , 'lr'))
            sys.exit()
        command = self.APP + " " + image + " " + image_name + " --dpi {0}".format(dpi)
        debug(command = command)
        self.run(command)
        #os.system(self.APP + " " + image + " " + image_name + " --dpi 2400")
        #os.system('cls')
        g = None
        with open(image_name + ".txt", 'rb') as f:
            if sys.version_info.major == 3:
                g = f.read().decode('utf-8')
            else:
                g = f.read()
        debug(g = g)
        #print("g =", g)
        nums = ''
        jenis = ''
        alamat = ''
        if g:
            nums = re.findall(".*?Nomor.*?:.*?(.*?)\n", g)
            if not nums:
                nums = re.findall(".*?No.*?:.*?(.*?)\n", g)#[0].strip()
            if nums:
                nums = nums[0].strip()
                nums = re.sub("\r", "", nums)
                nums = re.sub("_", "", nums)
            if not "/" in nums:
                try:
                    nums = re.findall('.*?No\.(.*?)\n', g)[0].strip()
                    nums = re.sub("\r", "", nums)
                    nums = re.sub("\)", "/", nums)
                except:
                    pass
            debug(nums = nums)
            jenis = re.findall(".*?SURAT(.*?)\n", g)
            if jenis:
                jenis = jenis[0].strip()
            
            alamat = re.findall(".*?PEMERINTAH(.*?)\n", g)
            if alamat:
                alamat = alamat[0].strip()
            
            
            random_a = ['A', 'B', 'C', 'D', 'E']
            random_a_num = random.randint(1111, 5466)
            random_suba = ['ay', 'bx', 'cw', 'fd', 'gg']
            random_suba_num = random.randint(200, 500)
            random_rak = ['IA', 'IIB', 'IIIC', 'IVD', 'VA', 'VIB', 'VIIC', 'VIIID', 'XVE', 'XA', 'XIB']
            random_rak_num = random.randint(600, 800)
            random_col = random.randint(896, 990)
            random_row = random.randint(433, 610)
            random_dinas = random.randint(555, 666)
            random_prov = random.randint(100, 300)
            random_kota = random.randint(400, 797)
            random_kec = random.randint(400, 797)
            random_desa = random.randint(110, 347)
            
            number = str(random.choice(random_a)) + str(random_a_num) + "/" + str(random.choice(random_suba)) + str(random_suba_num) + "/" + str(random.choice(random_rak)) + str(random_rak_num) + "/" + str(random_col) + "/" + str(random_row) + "/" + str(random_dinas) + "/" + str(random_prov) + "/" + str(random_kota) + "/" + str(random_kec) + "/" + str(random_desa) + "/" + self.now
            debug(number = number)
            print(make_colors("Nomor Document", 'lw', 'm') + " = " + make_colors(nums, 'lw', 'bl'))
            if jenis:
                print(make_colors("Jenis Document", 'b', 'lg') + " = " + make_colors("SURAT " + jenis, 'lw', 'bl'))
            else:
                print(make_colors("Jenis Document", 'lw', 'lr') + " = " + make_colors(jenis, 'lw', 'bl'))
            if alamat:
                print(make_colors("Kota/Kab/Prov ", 'b', 'ly') + " = " + make_colors("PEMERINTAH " + alamat, 'lw', 'bl'))
            else:
                print(make_colors("Kota/Kab/Prov ", 'lw', 'lr') + " = " + make_colors(alamat, 'lw', 'bl'))
            print(make_colors("Nomor Arsip   ", 'b', 'lc') + " = " + make_colors(number, 'lw', 'bl'))
            if not quiet:
                q = raw_input(make_colors("Insert to database [y/enter]: ", 'lw', 'lr'))
                if q == 'y':
                    self.insert_db([jenis, nums, alamat, number, g, image])
            else:
                self.insert_db([jenis, nums, alamat, number, g, image])
                
            return jenis, nums, alamat, number, g, image

    def scanning1(self, image = None):
        if image:
            img = cv2.imread(image)
        else:
            img = cv2.imread('card.jpg')
        width, height = 350, 250
        pst1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])
        pst2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(pst1, pst2)
        img_out = cv2.warpPerspective(img, matrix, (width, height))
        
        for x in range(0, 4):
            cv2.circle(img, (pst1[x][0], pst1[x][1]), 15, (0, 255, 0), cv2.FILLED)
            
        cv2.imshow("Origin", img)
        cv2.imshow("Output", img_out)
        cv2.waitKey(0)
        
        
if __name__ == '__main__':
    c = aiScanner()
    if len(sys.argv) > 1:
        c.scanning(sys.argv[1])
    else:
        c.scanning()
