import matplotlib.pyplot as plt
import cdcdata
import numpy as np
from scipy.interpolate import griddata
def cd_piont():
    c_data= cdcdata.cdcdata(r'H:\vscode\pythoncode\cdcdata\cdcdata\1.csv')
    plt.figure("CD散点图")

    plt.scatter(c_data.cd_x,c_data.cd_y)
    plt.axhline(y = 365000,xmin = -460000,xmax = 460000)
    plt.axhline(-365000,-460000,460000)
    plt.axvline(460000,-365000,365000)
    plt.axvline(-460000,-365000,365000)
    plt.autoscale()
    #plt.axhline(
    plt.xlim(-460000,460000)
    plt.ylim(-365000,365000)
    plt.show()



def cd_map():
    c_data= cdcdata.cdcdata(r'H:\vscode\pythoncode\cdcdata\cdcdata\1.csv')
    x = c_data.cd_x
    y = c_data.cd_y
    v = c_data.cd_val
    xg,yg = np.mgrid[min(x)+1:max(x)-1:100j,min(y)+1:max(y)-1:100j,]
    vg = griddata((x, y), v, (xg, yg), method='cubic')
    CS = plt.contourf(xg, yg, vg, 10, alpha = 0.75)#, cmap = plt.cm.hot)
    #CS = plt.contourf(xg, yg, vg,8, linewidth = 0.5)
    plt.clabel(CS, inline=0, fontsize=10)
    plt.xticks(())
    plt.yticks(())
    plt.show()

def tp_map():
    color_map = {1:'b',2:'g',3:'r',4:'c',5:'m',6:'y',7:'k',8:'w'}
    plt.figure("TP mapping图")
    c_data= cdcdata.cdcdata(r'H:\vscode\pythoncode\cdcdata\cdcdata\1.csv')
    x = c_data.tp_x_t
    y = c_data.tp_y_t
    dx = c_data.tp_dx
    dy = c_data.tp_dy
    c = c_data.tp_s
    for i in range(len(x)):
            plt.arrow(x[i],y[i],dx[i]*100000,dy[i]*100000,width = 1500,length_includes_head = True,head_width = 8000,color = color_map[c[i]])
    plt.xlim(-460000*1.5,460000*1.5)
    plt.ylim(-365000*1.5,365000*1.5)
    plt.show()





if __name__ == '__main__':
    tp_map()