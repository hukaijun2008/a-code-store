#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, QLabel,\
    QPushButton,QComboBox,QApplication)
import os
import spcReport

class windowmain(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        

        
        self.lbl_title = QLabel("欢迎使用SPC数据管理工具",self)
        
        app_path = r"\\172.22.100.52\武汉天马\面板厂\阵列部\PHOTO\全公司可读" +\
        r"\11.刘漫\00-过程管控\SPC管控"+"\\"
        
        self.combo_data  = QComboBox(self)
        self.combo_data.addItems(os.listdir(app_path + "报表\\"))
        
        self.combo_report = QComboBox(self)
        self.combo_report.addItems(os.listdir(app_path + "SPC\\"))
        
        self.but_data = QPushButton('分析数据', self)
        self.but_data.clicked.connect(self.but_data_click)
        
        self.but_report = QPushButton('打开报表', self)
        self.but_report.clicked.connect(self.but_report_click)
        
        self.but_refresh = QPushButton('刷新', self)
        self.but_refresh.clicked.connect(self.but_refresh_click)
        
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.lbl_title,0,1,1,5)
        grid.addWidget(self.but_refresh,0,0,1,1)
        grid.addWidget(self.combo_data,1,0,1,3)
        grid.addWidget(self.but_data,1,4,1,1)
        grid.addWidget(self.combo_report,2,0,1,3)
        grid.addWidget(self.but_report,2,4,1,1)

        
        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')   
        self.show()
    def but_data_click(self):
        spcReport.datefenxi(self.combo_data.currentText())
    def but_report_click(self):
        app_path = r"\\172.22.100.52\武汉天马\面板厂\阵列部\PHOTO\全公司可读" +\
        r"\11.刘漫\00-过程管控\SPC管控"+"\\"
        spcReport.open_report(app_path,self.combo_report.currentText())
    def but_refresh_click(self):
        app_path = r"\\172.22.100.52\武汉天马\面板厂\阵列部\PHOTO\全公司可读" +\
        r"\11.刘漫\00-过程管控\SPC管控"+"\\"
        self.combo_data.clear()
        self.combo_report.clear()
        self.combo_data.addItems(os.listdir(app_path + "报表\\"))
        self.combo_report.addItems(os.listdir(app_path + "SPC\\"))

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = windowmain()
    sys.exit(app.exec_())
