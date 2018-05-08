import csv


class cdcdata(object):
    def __init__(self,cdc_path):
        #变量初始化
        self.site = []
        self.cd_num = 0
        self.tp_num = 0
        self.ol_num = 0
        
        self.cd_x = []
        self.cd_y = []
        self.cd_z = []
        self.cd_val = []
        self.cd_spec = []
        
        self.tp_x = []
        self.tp_y = []
        self.tp_z = []
        self.tp_x_t = []
        self.tp_y_t = []
        self.tp_dx = []
        self.tp_dy = []
        self.tp_s = []

        self.ol_x = []
        self.ol_y = []
        self.ol_z = []
        self.ol_dx = []
        self.ol_dy = []
        #变量赋值
        with open(cdc_path) as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) < 3:
                    break
                if row[2] == '606' and len(self.site) == 0:
                    self.site.append(float(row[4]))
                    self.site.append(float(row[9]))
                    self.site.append(float(row[14]))
                if row[2] == '52':
                    self.cd_x.append(float(row[4]))
                    self.cd_y.append(float(row[9]))
                    self.cd_val.append(float(row[14]))
                    self.cd_z.append(float(row[19]))
                    self.cd_spec.append(float(row[15]))
                    self.cd_num = self.cd_num + 1
                if row[2] == '7':
                    self.cd_x.append(float(row[4]))
                    self.cd_y.append(float(row[9]))
                    self.cd_val.append(float(row[14]))
                    self.cd_z.append(float(row[24]))
                    self.cd_spec.append(float(row[15]))
                    self.cd_num = self.cd_num + 1
                if row[2] == '29':
                    self.tp_x.append(float(row[4]))
                    self.tp_x_t.append(float(row[5]))
                    self.tp_y.append(float(row[9]))
                    self.tp_y_t.append(float(row[10]))
                    self.tp_z.append(float(row[24]))
                    self.tp_dx.append(float(row[4])-float(row[5]))
                    self.tp_dy.append(float(row[9])-float(row[10]))
                    self.tp_s.append(float(row[28][9:]))
                    self.tp_num = self.tp_num + 1
                if row[2] == '151':
                    self.ol_x.append(float(row[4]))
                    self.ol_y.append(float(row[9]))
                    self.ol_dx.append(float(row[34]))
                    self.ol_dy.append(float(row[39]))
                    self.ol_num = self.ol_num + 1
                                      
    

if __name__ == '__main__':
    x = cdcdata(r'M:\software\testcode\dataview\1.csv')
    print(x.tp_dx)
