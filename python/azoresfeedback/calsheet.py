import matplotlib.pyplot as plt
import copy
import math
 
class calmode(object):
    def __init__(self,x_l,y_l,dx_l,dy_l):
        self.x_L = []
        self.y_L = []
        self.dx_L = []
        self.dy_L = []
        self.center = []
       
        for item_l in y_l:
            self.x_L.append(float(-item_l))
        for item_l in x_l:
            self.y_L.append(float(item_l))
        for item_l in dy_l:
            self.dx_L.append(float(item_l))
        for item_l in dx_l:
            self.dy_L.append(float(-item_l))
 
        self.center = [sum(self.x_L)/len(self.x_L),sum(self.y_L)/len(self.y_L)]
       
    def ol_map(self):
        color_map = {1:'b',2:'g',3:'r',4:'c',5:'m',6:'y',7:'k',8:'w'}
        plt.figure("OL mapping图")
        x = self.x_L
        y = self.y_L
        dx = self.dx_L
        dy = self.dy_L
        #c = c_data.tp_s
        plt.scatter(x, y)
        for i in range(len(x)):
            if dx[i] != 0 or dy[i] !=0:
                plt.arrow(x[i],y[i],dx[i]*50,dy[i]*50,width = 1.5,length_includes_head = True,head_width = 8,color = color_map[1])
        plt.xlim(-460*1.5,460*1.5)
        plt.ylim(-365*1.5,365*1.5)
        plt.show()  
 
    def shiftadj(self):
        con_aft = copy.deepcopy(self)
        shift_dx = sum(self.dx_L)/len(self.dx_L)
        shift_dy = sum(self.dy_L)/len(self.dy_L)
        con_aft.dx_L = [i - shift_dx for i in con_aft.dx_L]
        con_aft.dy_L = [i - shift_dy for i in con_aft.dy_L]
        print('OX:'+ str(shift_dx))
        print('OY:'+ str(shift_dy))
        return con_aft
 
   
    def thetaadj(self):
        con_aft = copy.deepcopy(self)
        
        thetay = 0
        num = 0

        for i in range(len(con_aft.x_L)):
            a = con_aft.x_L[i]- con_aft.center[0]
            if a != 0 :
                thetay += con_aft.dy_L[i] / a
                num += 1
        if thetay != 0:
            print('Thetay:'+str(thetay/num*1000))
        else:
            print('Thetay:0.0')
           
        thetax = 0
        num = 0
        for i in range(len(con_aft.x_L)):
            a = con_aft.y_L[i]- con_aft.center[1]
            if a != 0 :
                thetax += con_aft.dx_L[i] / a
                num += 1
        if thetax != 0:
            print('Thetax:'+str(thetax/num*1000))
        else:
            print('Thetax:0.0')
                               
    def thetaadj_new(self):
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
            if a != 0 :
                scalx += con_aft.dx_L[i] / a
                num += 1
        if num != 0:
            print('SX:'+str(scalx/num*1000))
        else:
            print('SX:0.0')
       
        scaly = 0
        num = 0
        for i in range(len(con_aft.y_L)):
            a = con_aft.y_L[i]- con_aft.center[1]
            if a != 0 :
                scaly += con_aft.dy_L[i] / (a)
                num += 1
        if num != 0:
            print('SY:'+str(scaly/num*1000))
        else:
            print('SY:0.0')
 
    def scaleadj_new(self):
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
 
if __name__ == '__main__':
    flag = 81
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
       
    print(flag)
    a = calmode(x,y,dx,dy)
    #b = a 
    b = a.shiftadj()
    b.thetaadj_new()
    b.scaleadj_new()
    #a.ol_map()
    b.ol_map()