import pandas as pd
import copy
import time
import numpy as np
import os
import shutil

class adcdata(object):
    def __init__(self,machine,orspec,desspec):

        file_ex = r'\\172.22.100.52\**\计测值' + '\\' + machine + '.log'
        #file_local = r'M:\software\testcode\CANON\A1PHT300.log'
        file_local = '.\\data\\' + machine + '.log'
        self.machine_name = machine
        self.orspec_in = orspec
        self.desspec_in = desspec
        flag_0 = 1
        self.linenum  = 0
        self.shotlist_key = pd.DataFrame()
        self.shotlist = {}
        self.error_stat = 'OK'
        self.shotlist_error = {}
        self.errorlist = pd.DataFrame()
        self.linenum_error = 0
        
        if os.path.exists(file_local):
            os.remove(file_local)

        shutil.copyfile(file_ex,file_local)
        try:
            self.df = pd.DataFrame(pd.read_csv(file_local,header=None))
            #不支持中文文件名及路径
        except:
            flag_0 = 0
            self.error_stat = 'NG'
            
        if flag_0 == 1:
            self.c16to10()
            
            self.splitshot()

            self.linenum = self.df.shape[0]
            self.begtime = self.df.at[0,3]
            self.endtime = self.df.at[self.linenum-1,3]

            
            self.errorjudge()
            self.linenum_error = self.errorlist.shape[0]
             

        
    def errorjudge(self):#判断计测正误，实例方法，目前考虑用均值方法，取前三片均值，后续值与均值差值不大于1.5，且前三片间差值不大于1.5
        #一片不判，2-3片判差值，三片以上与前三片比较
        for index1 in self.shotlist_key.index:
            
            tem_key = self.shotlist_key.at[index1]
            self.shotlist_error[tem_key] = pd.DataFrame()
            
            for i in range(5,17):
                tem_mean = self.shotlist[tem_key][i].mean()
                tem_max = self.shotlist[tem_key][i].max()
                tem_min = self.shotlist[tem_key][i].min()

                spec_max = tem_mean + self.orspec_in
                spec_min = tem_mean - self.orspec_in

                if tem_max < spec_max  and tem_min >spec_min:
                    continue
                self.shotlist_error[tem_key] = self.shotlist_error[tem_key].append(self.shotlist[tem_key][self.shotlist[tem_key][i] > spec_max])
                self.shotlist_error[tem_key] = self.shotlist_error[tem_key].append(self.shotlist[tem_key][self.shotlist[tem_key][i] < spec_min])
            for i in range(17,23):
                tem_mean = self.shotlist[tem_key][i].mean()
                tem_max = self.shotlist[tem_key][i].max()
                tem_min = self.shotlist[tem_key][i].min()

                spec_max = tem_mean + self.desspec_in
                spec_min = tem_mean - self.desspec_in

                if tem_max < spec_max  and tem_min >spec_min:
                    continue
                self.shotlist_error[tem_key] = self.shotlist_error[tem_key].append(self.shotlist[tem_key][self.shotlist[tem_key][i] > spec_max])
                self.shotlist_error[tem_key] = self.shotlist_error[tem_key].append(self.shotlist[tem_key][self.shotlist[tem_key][i] < spec_min])
            
            if self.shotlist_error[tem_key].shape[0] != 0:
                self.shotlist_error[tem_key] = self.shotlist_error[tem_key][~self.shotlist_error[tem_key].duplicated()]
            #print(self.shotlist_error[tem_key])
            self.errorlist = self.errorlist.append(self.shotlist_error[tem_key])

                



    def splitshot(self):
        self.shotlist_key = self.df[2]
        self.shotlist_key = self.shotlist_key[~self.shotlist_key.duplicated()]
        for index1 in self.shotlist_key.index:
            tem_key = self.shotlist_key.at[index1]
            self.shotlist[tem_key] = copy.deepcopy(self.df)
            self.shotlist[tem_key] = self.shotlist[tem_key][self.shotlist[tem_key][2] == tem_key]


        
        
    def c16to10(self):
        
        for i in range(17,32):
            del self.df[i]
        self.df[self.df == '********'] = np.nan
        self.df = self.df.dropna(axis=0,how='any')
        
        for column1 in self.df.columns:
            for index1 in self.df.index:
                if str(self.df.at[index1,column1])[0] != 'f':
                    self.df.at[index1,column1] = int(str(self.df.at[index1,column1]),16)
                    
                else:
                    text16 = ''
                    for i in range(len(str(self.df.at[index1,column1]))):
                        text16 = text16 + 'f'
                    self.df.at[index1,column1] = int(str(self.df.at[index1,column1]),16) -int(str(text16),16)-1 

        for index1 in self.df.index:
            timeStruct = time.localtime(self.df.at[index1,3] + 3600)
            self.df.at[index1,3] = time.strftime('%Y/%m/%d %H:%M:%S',timeStruct)
        for i in range(6):
            col_new = i + 17
            if i == 0 or i == 1:
                col_1 = i + 5
                col_2 = i + 7
            if i == 2 or i == 3:
                col_1 = i + 7
                col_2 = i + 9
            if i == 4 or i == 5:
                col_1 = i + 9
                col_2 = i + 11
            self.df[col_new] = self.df[col_2] - self.df[col_1]
        
    def toexcel(self):
        timeStruct = time.strptime(self.begtime,'%Y/%m/%d %H:%M:%S')
        strbeg = time.strftime('%Y%m%d%H%M%S',timeStruct)
        timeStruct = time.strptime(self.endtime,'%Y/%m/%d %H:%M:%S')
        strend = time.strftime('%Y%m%d%H%M%S',timeStruct)
        
        file_path = 'T:\\**\\'
        file_path = file_path + self.machine_name + '\\' + strbeg + '.xlsx'
        if ~os.path.exists(file_path):
            writer = pd.ExcelWriter(file_path)
            for index1 in self.shotlist_key.index:
                tem_key = self.shotlist_key.at[index1]
                self.shotlist[tem_key].to_excel(writer,str(tem_key))
            
                
            self.errorlist.to_excel(writer,'error')
            writer.save()
     

if __name__ == '__main__':
    optionfile = open(r'.\data\option.txt')
    print(optionfile.readline()[:-1])
    orspec = int(optionfile.readline()[:-1])
    print(orspec)
    print(optionfile.readline()[:-1])
    desspec = int(optionfile.readline()[:-1])
    print(desspec)
    print(optionfile.readline()[:-1])
    cyccletime = int(optionfile.readline())
    print(cyccletime)
    
    if True:
        print('将开始抓取误计测数据')
        time.sleep(1)
        print('5')
        time.sleep(1)
        print('4')
        time.sleep(1)
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        
        a1pht100 = adcdata('A1PHT100',orspec,desspec)
        if a1pht100.error_stat == 'OK':
            if a1pht100.errorlist.shape[0] != 0:
                a1pht100.toexcel()
                print('A1PHT100')
                print(a1pht100.errorlist)
            else:
                print('A1PHT100 暂无误计测')
                    
        a1pht300 = adcdata('A1PHT300',orspec,desspec)
        if a1pht300.error_stat == 'OK':
            if a1pht300.errorlist.shape[0] != 0:
                a1pht300.toexcel()
                print('A1PHT300')
                print(a1pht300.errorlist)
            else:
                print('A1PHT300 暂无误计测')
         
        a1pht500 = adcdata('A1PHT500',orspec,desspec)
        if a1pht500.error_stat == 'OK':  
            if a1pht500.errorlist.shape[0] != 0:
                a1pht500.toexcel()
                print('A1PHT500')
                print(a1pht500.errorlist)
            else:
                print('A1PHT500 暂无误计测')

        old_a1pht100 = a1pht100
        old_a1pht300 = a1pht300
        old_a1pht500 = a1pht500
        
        while True:
            timeStruct = time.localtime(time.time())
            timenow = time.strftime('%Y%m%d%H%M%S',timeStruct)
            print(timenow)
            for i in range(cyccletime):
                time.sleep(1)

            a1pht100 = adcdata('A1PHT100',orspec,desspec)
            if a1pht100.error_stat == 'OK':  
                if a1pht100.linenum == old_a1pht100.linenum:
                    old_a1pht100 = a1pht100
                    pass
                elif a1pht100.linenum > old_a1pht100.linenum:
                    old_a1pht100 = a1pht100
                    if a1pht100.linenum_error > old_a1pht100.linenum_error:
                        a1pht100.toexcel()
                        print('A1PHT100新误计测，请关注')
                        print(a1pht100.errorlist)
                elif a1pht100.linenum < old_a1pht100.linenum and a1pht100.linenum < 3:
                    old_a1pht100.toexcel()
                    old_a1pht100 = a1pht100
                    print('A1PHT100已切换新产品，上一款计测值已存为Excel')
                    if a1pht100.errorlist.shape[0] != 0:
                        a1pht100.toexcel()
                        print(a1pht100.errorlist)
                    else:
                        print('A1PHT100 暂无误计测')
                    
            a1pht300 = adcdata('A1PHT300',orspec,desspec)
            if a1pht300.error_stat == 'OK':  
                if a1pht300.linenum == old_a1pht300.linenum:
                    old_a1pht300 = a1pht300
                    pass
                elif a1pht300.linenum > old_a1pht300.linenum:
                    old_a1pht300 = a1pht300
                    if a1pht300.linenum_error > old_a1pht300.linenum_error:
                        a1pht300.toexcel()
                        print('A1PHT300新误计测，请关注')
                        print(a1pht300.errorlist)
                elif a1pht300.linenum < old_a1pht300.linenum and a1pht300.linenum < 3:
                    old_a1pht300.toexcel()
                    old_a1pht300 = a1pht300
                    print('A1PHT300已切换新产品，上一款计测值已存为Excel')
                    if a1pht300.errorlist.shape[0] != 0:
                        a1pht300.toexcel()
                        print(a1pht300.errorlist)
                    else:
                        print('A1PHT300 暂无误计测')
                    
            a1pht500 = adcdata('A1PHT500',orspec,desspec)
            if a1pht500.error_stat == 'OK':  
                if a1pht500.linenum == old_a1pht500.linenum:
                    old_a1pht500 = a1pht500
                    pass
                elif a1pht500.linenum > old_a1pht500.linenum:
                    old_a1pht500 = a1pht500
                    if a1pht500.linenum_error > old_a1pht500.linenum_error:
                        a1pht500.toexcel()
                        print('A1PHT500新误计测，请关注')
                        print(a1pht500.errorlist)
                elif a1pht500.linenum < old_a1pht500.linenum  and a1pht500.linenum < 3:
                    old_a1pht500.toexcel()
                    old_a1pht500 = a1pht500
                    print('A1PHT500已切换新产品，上一款计测值已存为Excel')
                    if a1pht500.errorlist.shape[0] != 0:
                        a1pht500.toexcel()
                        print(a1pht500.errorlist)
                    else:
                        print('A1PHT500 暂无误计测')
            
        
        
  
        
