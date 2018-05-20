import matplotlib.pyplot as plt
import copy
import math
import numpy as np
import mapdata
import oldata
class calmode(object):
    def __init__(self,x_l,y_l,dx_l,dy_l):
        self.x_L = x_l
        self.y_L = y_l
        self.dx_L = dx_l
        self.dy_L = dy_l
        self.region_L = []
        self.center = []
        self.adj_result = {}
        self.OffsetX = 0
        self.OffsetY = 0
        self.Theta = 0
        self.Orth = 0
        self.ScaleX = 0
        self.ScaleY = 0
        for i in range(len(self.x_L)):
            self.region_L.append(0)
        #for item_l in y_l:
            #self.x_L.append(float(-item_l))
        #for item_l in x_l:
            #self.y_L.append(float(item_l))
        #for item_l in dy_l:
            #self.dx_L.append(float(item_l))
        #for item_l in dx_l:
            #self.dy_L.append(float(-item_l))
 
        self.center = {}
    def regionjudge(self,mapdata):
        for i in range(len(self.x_L)):
            for region_id in mapdata.regin_info:
                cx = mapdata.regin_info[region_id]['RX']
                cy = mapdata.regin_info[region_id]['RY']
                wx = mapdata.regin_info[region_id]['RW']
                wy = mapdata.regin_info[region_id]['RH']
                if self.x_L[i] > cx - wx/2 and self.x_L[i] < cx + wx/2:
                    if self.y_L[i] > cy - wy/2 and self.y_L[i] < cy + wy/2:
                        self.region_L[i] = region_id
                        break
        for region_id in mapdata.regin_info:
            self.adj_result[region_id] = {}
        print(self.adj_result)
    def ol_map(self,FlieName):
        color_map = {'0':'b','1':'g','2':'r','3':'c','4':'m','5':'y','6':'k','7':'w'}
        plt.figure("OL mapping图")
        x = self.x_L
        y = self.y_L
        dx = self.dx_L
        dy = self.dy_L
        #c = c_data.tp_s
       
        for i in range(len(x)):
            plt.scatter(x[i], y[i],s = 10,color = color_map[self.region_L[i]])
            if dx[i] != 0 or dy[i] !=0:
                plt.arrow(x[i],y[i],dx[i]*50,dy[i]*50,width = 1.5,length_includes_head = True,head_width = 8,color = color_map[self.region_L[i]])
        plt.xlim(-460*1.5,460*1.5)
        plt.ylim(-365*1.5,365*1.5)
        plt.savefig( FlieName + ".jpg")  
        plt.close('all')
        #plt.show()  
 
    def shiftadj(self):
        con_aft = copy.deepcopy(self)
        region_dic = {}
        for i in range(len(con_aft.region_L)):
            if con_aft.region_L[i] in region_dic:
                region_dic[con_aft.region_L[i]].append(i)
            else:
                region_dic[con_aft.region_L[i]] = [i]
        print(region_dic)
        for key_region in region_dic:
            dx_total = 0
            dy_total = 0
            x_total = 0
            y_total = 0
            for i in region_dic[key_region]:
                dx_total += self.dx_L[i]
                dy_total += self.dy_L[i]
                x_total += self.x_L[i]
                y_total += self.y_L[i]

            shift_dx = dx_total/len(region_dic[key_region])
            shift_dy = dy_total/len(region_dic[key_region])
            center_x = x_total/len(region_dic[key_region])
            center_y = y_total/len(region_dic[key_region])
            con_aft.center[key_region] = [center_x,center_y]
            con_aft.adj_result[key_region]['OffsetX'] = shift_dx
            con_aft.adj_result[key_region]['OffsetY'] = shift_dy
            con_aft.adj_result[key_region]['center'] = [center_x,center_y]

            for i in region_dic[key_region]:
                con_aft.dx_L[i] = con_aft.dx_L[i] - shift_dx
                con_aft.dy_L[i] = con_aft.dy_L[i] - shift_dy
        
            print('OX:'+ str(shift_dx))
            print('OY:'+ str(shift_dy))

        return con_aft
 
   
    
    def thetaadj(self):
        con_aft = copy.deepcopy(self)
        
        thetay = 0
        num = 0

        for i in range(len(con_aft.x_L)):
            a = con_aft.x_L[i]- con_aft.center[0]
            thetay += con_aft.dy_L[i] * a
            num += a**2
        if num != 0:
            print('Thetay:'+str(thetay/num*1000))
        else:
            print('Thetay:0.0')

           
        thetax = 0
        num = 0
        for i in range(len(con_aft.x_L)):
            a = con_aft.y_L[i]- con_aft.center[1]
            thetax += con_aft.dx_L[i] * a
            num += a**2
        if num != 0:
            print('Thetax:'+str(thetax/num*1000))
        else:
            print('Thetax:0.0')
   

    def scaleadj(self):
        con_aft = copy.deepcopy(self)
        scalx = 0
        num = 0
        for i in range(len(con_aft.x_L)):
            a = con_aft.x_L[i]- con_aft.center[0]
            
            scalx += con_aft.dx_L[i] * a
            num += a**2
        if num != 0:
            print('SX:'+str(scalx/num*1000))
        else:
            print('SX:0.0')
       
        scaly = 0
        num = 0
        for i in range(len(con_aft.y_L)):
            a = con_aft.y_L[i]- con_aft.center[1]
            scaly += con_aft.dy_L[i] * (a)
            num += a**2
        if num != 0:
            print('SY:'+str(scaly/num*1000))
        else:
            print('SY:0.0')
    def mincal(self):
        
        con_aft = copy.deepcopy(self)
        region_dic = {}
        for i in range(len(con_aft.region_L)):
            if con_aft.region_L[i] in region_dic:
                region_dic[con_aft.region_L[i]].append(i)
            else:
                region_dic[con_aft.region_L[i]] = [i]

        for key_region in region_dic:

            Co_a = [[0.0,0.0],[0.0,0.0]]
            Co_b = [0.0,0.0]
            for i in region_dic[key_region]:
                Co_a[1][1] += (con_aft.x_L[i]-con_aft.center[key_region][0])**2
                Co_a[0][1] += (con_aft.x_L[i]-con_aft.center[key_region][0])*(con_aft.y_L[i]-con_aft.center[key_region][1])
                Co_a[1][0] += (con_aft.x_L[i]-con_aft.center[key_region][0])*(con_aft.y_L[i]-con_aft.center[key_region][1])
                Co_a[0][0] += (con_aft.y_L[i]-con_aft.center[key_region][1])**2
                Co_b[0] += con_aft.dy_L[i]*(con_aft.y_L[i]-con_aft.center[key_region][1])
                Co_b[1] += con_aft.dy_L[i]*(con_aft.x_L[i]-con_aft.center[key_region][0])
            a = np.array(Co_a)
            b = np.array(Co_b)
            ans_L = np.linalg.solve(a,b)
            con_aft.Scaly = ans_L[0]
            con_aft.Theta = ans_L[1]
        

        
            Co_a = [[0.0,0.0],[0.0,0.0]]
            Co_b = [0.0,0.0]
            for i in region_dic[key_region]:
                Co_a[0][0] += (con_aft.x_L[i]-con_aft.center[key_region][0])**2
                Co_a[0][1] += (con_aft.x_L[i]-con_aft.center[key_region][0])*(con_aft.y_L[i]-con_aft.center[key_region][1])
                Co_a[1][0] += (con_aft.x_L[i]-con_aft.center[key_region][0])*(con_aft.y_L[i]-con_aft.center[key_region][1])
                Co_a[1][1] += (con_aft.y_L[i]-con_aft.center[key_region][1])**2
                Co_b[0] += con_aft.dx_L[i]*(con_aft.x_L[i]-con_aft.center[key_region][0])
                Co_b[1] += con_aft.dx_L[i]*(con_aft.y_L[i]-con_aft.center[key_region][1])
            a = np.array(Co_a)
            b = np.array(Co_b)
            ans_L = np.linalg.solve(a,b)
            con_aft.Scalx = ans_L[0]
            con_aft.Orth = ans_L[1] + con_aft.Theta
            
            con_aft.adj_result[key_region]['Theta'] = con_aft.Theta*1000
            con_aft.adj_result[key_region]['Scalx'] = con_aft.Scalx*1000
            con_aft.adj_result[key_region]['Scaly'] = con_aft.Scaly*1000
            con_aft.adj_result[key_region]['Orth'] = con_aft.Orth*1000
            
            
            print("Theta:"+ str(con_aft.Theta*1000))
            print("Scalx:"+ str(con_aft.Scalx*1000))
            print("Scaly:"+ str(con_aft.Scaly*1000))
            print("Orth:"+ str(con_aft.Orth*1000))

            for i in region_dic[key_region]:
                con_aft.dx_L[i] = con_aft.dx_L[i] - con_aft.Scalx * (con_aft.x_L[i]-con_aft.center[key_region][0]) \
                                  -(con_aft.Orth-con_aft.Theta) * (con_aft.y_L[i]-con_aft.center[key_region][1])
                con_aft.dy_L[i] = con_aft.dy_L[i] - con_aft.Scaly * (con_aft.y_L[i]-con_aft.center[key_region][1]) \
                                  -con_aft.Theta * (con_aft.x_L[i]-con_aft.center[key_region][0])
        return con_aft
if __name__ == '__main__':
    flag = 99
    if flag == 1: # OX 0 OY -0.75 T 13.514 SX 0 SY 13.514 Orth 13.514
        x = [-211,-211,-100,-100]
        y = [211,100,100,211]
        dx = [3,0,0,0]
        dy = [0,0,0,0]
    if flag == 2: # OX 0 OY -0.75 T 0 SX 0 SY -30 Orth 0
        x = [-100,-200,-150,-150]
        y = [150,150,100,200]
        dx = [3,0,0,0]
        dy = [0,0,0,0]
    if flag == 3: # OX 0 OY -0.75 T 5 SX 0 SY 25 Orth 5
        x = [-200,-150,-100,-100]
        y = [200,150,100,200]
        dx = [3,0,0,0]
        dy = [0,0,0,0]
    if flag == 4: # OX 0 OY -0.75 T 30 SX 0 SY 30 Orth 30
        x = [-200,-150,-150,-100]
        y = [200,150,150,200]
        dx = [3,0,0,0]
        dy = [0,0,0,0]
    if flag == 5: # OX 0 OY -1.5 T 30 SX 0 SY 0 Orth 0
        x = [-200,-200]
        y = [200,100]
        dx = [3,0]
        dy = [0,0]
    if flag == 6: # OX 0 OY -0.75 T 5.511 SX 0 SY 7.496 Orth 5.511
        x = [-300,-300,-100,-11.9176]
        y = [400,100,100,440.0523]
        dx = [3,0,0,0]
        dy = [0,0,0,0]
    if flag == 7: # OX 0 OY -1 T 0 SX 0 SY 30 Orth 0
        x = [-200,-100,-100]
        y = [200,200,100]
        dx = [3,0,0]
        dy = [0,0,0]
       
    if flag == 8: # OX 1 OY 0 T 0 SX 0 SY 0 Orth -30
        x = [-200,-100,-100]
        y = [200,200,100]
        dx = [0,0,0]
        dy = [3,0,0]
    if flag == 81: # OX 0 OY -1 T 0 SX 0 SY 30 Orth 0
        x = [-200,-100,-100]
        y = [200,200,100]
        dx = [3,0,0]
        dy = [0,0,0]

    if flag == 9: # OX 0 OY -0.75 T 4.615 SX 0 SY 8.654 Orth 4.615
        x = [-300,-300,-100,-100]
        y = [300,100,100,400]
        dx = [3,0,0,0]
        dy = [0,0,0,0]
 
    if flag == 10: # OX 0 OY 0 T 60 SX 0 SY 0 Orth 0
        x = [-200,-200,-100,-100]
        y = [200,100,200,100]
        dx = [3,-3,3,-3]
        dy = [3,3,-3,-3]
    if flag == 11: # OX 0 OY 0 T 60 SX 0 SY 0 Orth 0
        x = [-150,-150,-100,-100]
        y = [200,100,200,100]
        dx = [3,-3,3,-3]
        dy = [1.5,1.5,-1.5,-1.5]
       
    if flag == 12: # OX 0 OY -2 T 0 SX 0 SY 0 Orth -30
        x = [-200,-190,-200]
        y = [200,150,100]
        dx = [3,0,3]
        dy = [0,0,0]
    if flag == 13: # OX 0 OY -1 T 30 SX 0 SY -500 Orth 30
        x = [-200,-203,-200]
        y = [200,150,100]
        dx = [3,0,0]
        dy = [0,0,0]
    if flag == 14: # OX 0 OY -1 T 23.077 SX 0 SY 0 Orth 23.077
        x = [-200,-200,-200]
        y = [200,175,100]
        dx = [3,0,0]
        dy = [0,0,0]
    if flag == 15: # OX 0 OY -1 T 30 SX 0 SY 0 Orth 30
        x = [-200,-200,-200]
        y = [200,150,100]
        dx = [3,0,0]
        dy = [0,0,0]
 
    if flag == 16: # OX 0 OY -0.75 T 30 SX 0 SY -1000 Orth 30
        x = [-200,-200,-200,-201]
        y = [200,150,100,150]
        dx = [3,0,0,0]
        dy = [0,0,0,0]
 
 
    if flag == 17: # OX 0 OY -0.75 T 24 SX 0 SY 0 Orth 24
        x = [-200,-200,-200,-200]
        y = [200,125,100,175]
        dx = [3,0,0,0]
        dy = [0,0,0,0]
    if flag == 18: # OX 0.75 OY 0 T 0 SX -25 SY 0 Orth -5
        x = [-200,-200,-150,-100]
        y = [200,100,150,100]
        dx = [0,0,0,0]
        dy = [3,0,0,0]
    if flag == 99:
        #mapobj = mapdata.mapata(r'C:\Users\Administrator\Desktop\hkj\275_site_correction_map1')
        #olobj = oldata.oldata(r'C:\Users\Administrator\Desktop\hkj\1.csv')
        mapobj = mapdata.mapata(r'M:\调查中事项\OL\hkj\663_site_correction_map')
        olobj = oldata.oldata(r'M:\调查中事项\OL\hkj\OL20180502160842.csv')

    a = calmode(olobj.oldata_x,olobj.oldata_y,olobj.oldata_dx,olobj.oldata_dy)
    a.regionjudge(mapobj)
    a.ol_map('1')
    b = a.shiftadj()
    #b.ol_map()
    c = b.mincal()
    #c.ol_map()
    print(c.adj_result)

    #a = calmode(x,y,dx,dy)
    #b = a 
    #b = a.shiftadj()
    #c = b.mincal()
    #b.thetaadj()
    #b.scaleadj()
    #a.ol_map()
    #c.ol_map()
