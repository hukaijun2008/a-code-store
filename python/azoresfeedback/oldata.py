import matplotlib.pyplot as plt
class oldata(object):
    def __init__(self,file_path):
        self.reci_num = ''
        self.glassid = ''
        self.time = ''
        self.point = 0
        self.oldata_x = []
        self.oldata_y = []
        self.oldata_dx = []
        self.oldata_dy = []
        self.readfile(file_path)

    def readfile(self,file_path):
        iter_file = open(file_path)
        for text in iter_file.readlines():
            text_s = text.split(',')
            if text_s[0] == 'Recipe No.':
                self.reci_num = text_s[1][:-1]
            elif text_s[0] == 'Glass ID':
                self.glassid = text_s[1][:-1]
            elif text_s[0] == 'Insp. Date':
                self.time = text_s[1][:-1]
            elif text_s[0] == 'Measure Point':
                self.point = text_s[1][:-1]
            else:
                self.oldata_x.append(-float(text_s[2]))
                self.oldata_y.append(float(text_s[1]))
                self.oldata_dx.append(float(text_s[4]))
                self.oldata_dy.append(-float(text_s[3]))
            
     


if __name__ == '__main__':
    a = oldata(r'C:\Users\Administrator\Desktop\hkj\1.csv')
    #a = oldata(r'C:\Users\Administrator\Desktop\hkj\新建文件夹\OL20180429175018.csv')
   
        
