import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import calsheet
import mapdata
import oldata

class steppermatch(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.but_data = QPushButton('选择数据文件', self)
        self.but_data.clicked.connect(self.but_data_click)

        self.line_data  = QLineEdit('')

        self.but_map = QPushButton('选择map文件', self)
        self.but_map.clicked.connect(self.but_map_click)

        self.line_map  = QLineEdit('')

        self.but_load = QPushButton('Load', self)
        self.but_load.clicked.connect(self.but_load_click)

        self.lbl_pix1 = QLabel(self)
        self.lbl_pix2 = QLabel(self)
        self.pixmap1 = QPixmap('')
        self.pixmap2 = QPixmap('')
        self.lbl_pix1.setPixmap(self.pixmap1)
        self.lbl_pix2.setPixmap(self.pixmap2)


        self.cal_list=QStandardItemModel(0,7)
        self.cal_list.setHorizontalHeaderLabels(['区域','OffsetX', \
                                                 'OffsetY','Theta','Scalx','Scaly','Orth'])
        self.tableView=QTableView()
        self.tableView.setModel(self.cal_list)
        self.tableView.resizeColumnsToContents()


        
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.but_data,0,0,1,1)
        grid.addWidget(self.line_data,0,1,1,4)
        grid.addWidget(self.but_load,0,5,1,1)
        grid.addWidget(self.but_map,1,0,1,1)
        grid.addWidget(self.line_map,1,1,1,4)
        grid.addWidget(self.lbl_pix1,2,0,1,3)
        grid.addWidget(self.lbl_pix2,2,3,1,3)
        grid.addWidget(self.tableView,3,0,1,5)
        

        

        
        self.setLayout(grid)

        
        self.setGeometry(60, 60, 1200, 800)        
        self.setWindowTitle("Stepper match-个人版")
        self.show()
        
    def but_data_click(self):
        fileName,filetype=QFileDialog.getOpenFileName(self,"选择文件",'M:\\',"(*.csv)")
        self.line_data.setText(fileName)
        
    def but_map_click(self):
        fileName,filetype=QFileDialog.getOpenFileName(self,"选择文件",'M:\\',"(*)")
        self.line_map.setText(fileName)

    def but_load_click(self):
        mapobj = mapdata.mapata(self.line_map.displayText())
        olobj = oldata.oldata(self.line_data.displayText())
        a = calsheet.calmode(olobj.oldata_x,olobj.oldata_y,olobj.oldata_dx,olobj.oldata_dy)
        a.regionjudge(mapobj)
        a.ol_map('1')
        b = a.shiftadj()
        b.ol_map('2')
        c = b.mincal()
        c.ol_map('3')


        
        self.pixmap1.load('1.jpg')
        self.pixmap2.load('2.jpg')
        self.lbl_pix1.setPixmap(self.pixmap1)
        self.lbl_pix2.setPixmap(self.pixmap2)

        self.cal_list=QStandardItemModel(len(c.adj_result),7)
        self.cal_list.setHorizontalHeaderLabels(['区域','OffsetX', \
                                                 'OffsetY','Theta','Scalx','Scaly','Orth'])
        self.tableView.setModel(self.cal_list)
        self.tableView.resizeColumnsToContents()
        
        row_num = 0
        for region_id in c.adj_result:
            self.cal_list.setItem(row_num, 0, QStandardItem(region_id))
            #self.cal_list.setItem(row_num, 1, QStandardItem(str(c.adj_result[region_id]['center'][0])))
            #self.cal_list.setItem(row_num, 2, QStandardItem(str(c.adj_result[region_id]['center'][1])))
            self.cal_list.setItem(row_num, 1, QStandardItem(str(c.adj_result[region_id]['OffsetX'])))
            self.cal_list.setItem(row_num, 2, QStandardItem(str(c.adj_result[region_id]['OffsetY'])))
            self.cal_list.setItem(row_num, 3, QStandardItem(str(c.adj_result[region_id]['Theta'])))
            self.cal_list.setItem(row_num, 4, QStandardItem(str(c.adj_result[region_id]['Scalx'])))
            self.cal_list.setItem(row_num, 5, QStandardItem(str(c.adj_result[region_id]['Scaly'])))
            self.cal_list.setItem(row_num, 6, QStandardItem(str(c.adj_result[region_id]['Orth'])))
            
            
            row_num = row_num + 1
        self.tableView.resizeColumnsToContents()


        
       

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = steppermatch()
    sys.exit(app.exec_())
