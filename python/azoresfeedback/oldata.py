import matplotlib.pyplot as plt
class oldata(object):
    def __init__(self,file_path):
        self.reci_num = ''
        self.glassid = ''
        self.time = ''
        self.point = 0
        self.oldata_x = {}
        self.oldata_y = {}
        self.oldata_dx = {}
        self.oldata_dy = {}
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
                self.oldata_x[int(text_s[0])] = float(text_s[1])
                self.oldata_y[int(text_s[0])] = float(text_s[2])
                self.oldata_dx[int(text_s[0])] = float(text_s[3])
                self.oldata_dy[int(text_s[0])] = float(text_s[4])
            
    def ol_map(self):
        color_map = {1:'b',2:'g',3:'r',4:'c',5:'m',6:'y',7:'k',8:'w'}
        plt.figure("OL mapping图")
        x = self.oldata_x
        y = self.oldata_y
        dx = self.oldata_dx
        dy = self.oldata_dy
        #c = c_data.tp_s
        for i in range(1,len(x)+1):
            if dx[i] != 0 or dy[i] !=0:
                plt.arrow(x[i],y[i],dx[i]*100,dy[i]*100,width = 1.5,length_includes_head = True,head_width = 8,color = color_map[1])
        plt.xlim(-460*1.5,460*1.5)
        plt.ylim(-365*1.5,365*1.5)
        plt.show()      
     


if __name__ == '__main__':
    a = oldata(r'C:\Users\Administrator\Desktop\hkj\1.csv')
    #a = oldata(r'C:\Users\Administrator\Desktop\hkj\新建文件夹\OL20180429175018.csv')
    a.ol_map()
        
