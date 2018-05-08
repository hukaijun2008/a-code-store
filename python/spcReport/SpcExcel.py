import logging
logging.basicConfig(filename="M:\\spc.log",level=logging.DEBUG,format="%(asctime)s - %(levelname)s - %(message)s")
logging.disable(logging.CRITICAL)
import pandas as pd
import os
import shutil
import openpyxl
import win32com.client
import copy

class SpcExcelArray(object):
    #读取报表，数据保存在e_array
    def __init__(self,report_name,spc_sheet_name,app_path):
        spc_report_path = app_path+ "报表"+"\\" + report_name
        self.e_array = pd.DataFrame(pd.read_excel(spc_report_path,sheet_name = spc_sheet_name,header = 3))
        self.e_array_e_point = pd.DataFrame()
        self.e_array_e_ave = pd.DataFrame()
        self.e_array_e_all = pd.DataFrame()
        self.report_name_self = report_name
        self.sheet_name_self = spc_sheet_name
        self.app_path_self = app_path
        self.station_self = ""
        self.item_self = ""
    #筛选，筛选条件为station和item
    def spcfilter(self,station = "ALL",spc_item = "ALL"):
        e_array_tem = copy.deepcopy(self)
        e_array_tem.station_self = station
        e_array_tem.item_self = spc_item
        if station != "ALL":
            e_array_tem.e_array = e_array_tem.e_array[e_array_tem.e_array["OPER"]==int(station)]
            
        logging.info(station + str(e_array_tem.e_array.shape))
        
        if spc_item != "ALL":
            e_array_tem.e_array = e_array_tem.e_array[e_array_tem.e_array["ITEM"]==spc_item]
        logging.info(spc_item + str(e_array_tem.e_array.shape))
        
    #对是否超标进行判断，通过Item判断，进行判断，获得超标列表，实例方法
    
        e_array_tem.e_array_e_point = e_array_tem.e_array[(e_array_tem.e_array["MAX"] > e_array_tem.e_array["USL"]) | \
                                        (e_array_tem.e_array["MIN"] < e_array_tem.e_array["LSL"])]
        e_array_tem.e_array_e_ave = e_array_tem.e_array[(e_array_tem.e_array["AVARAGE"] > e_array_tem.e_array["UCL"]) | \
                                        (e_array_tem.e_array["AVARAGE"] < e_array_tem.e_array["LCL"])]
        
        e_array_tem.e_array_e_all = copy.deepcopy(e_array_tem.e_array_e_ave)
        e_array_tem.e_array_e_all = e_array_tem.e_array_e_all.append(e_array_tem.e_array_e_point)
        e_array_tem.e_array_e_all = e_array_tem.e_array_e_all.drop_duplicates()
        return e_array_tem
        

    #向excel导出，需要修改，改为一次输出多个sheet，改为公共方法，参数为列表
    def e_array2excel(self,arraylist):
        spc_moban_path = self.app_path_self + "报表模板.xlsm"
        
        spc_excel_path = self.app_path_self + "SPC"+"\\"+ self.report_name_self
        spc_excel_path = spc_excel_path[:-4] + ".xlsm"
        
        spc_data_path = self.app_path_self + "data\\" + self.report_name_self[:-4] +"数据.xlsx"
        writer = pd.ExcelWriter(spc_data_path)
        sum_chat = []
        eall = pd.DataFrame()
        for key,value in arraylist.items():
            value.e_array.to_excel(writer,key)
            value.e_array_e_all.to_excel(writer,"e" + key)
            sum_chat.append([key,value.e_array.shape[0],value.e_array_e_point.shape[0],\
                             value.e_array_e_ave.shape[0],value.e_array_e_all.shape[0]]) 
            eall = eall.append(value.e_array_e_all)
        eall.to_excel(writer,"e_all")
        pd.DataFrame(sum_chat).to_excel(writer,"目录data")
        
        writer.save()


        
        if os.path.exists(spc_excel_path) == False:
            pass
            shutil.copyfile(spc_moban_path,spc_excel_path)
        xlapp = win32com.client.Dispatch('excel.application')
        xlapp.visible=1
        xlbook = xlapp.workbooks.open(spc_excel_path)

        
    
if __name__ == "__main__":
    pass


