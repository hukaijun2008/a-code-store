import logging
logging.basicConfig(filename="M:\\spc.log",level=logging.DEBUG,format="%(asctime)s - %(levelname)s - %(message)s")
import SpcExcel
import pandas as pd
import numpy as np
import win32com.client

def datefenxi(report_name):


    
    app_path = r"\\172.22.100.52\武汉天马\面板厂\阵列部\PHOTO\全公司可读" +\
        r"\11.刘漫\00-过程管控\SPC管控"+"\\"
    array_mulu = pd.DataFrame(pd.read_excel(app_path + "报表模板.xlsm",sheet_name ="目录",header = 0))
    excel_cdc = SpcExcel.SpcExcelArray(report_name,"CDC",app_path)
    excel_prf = SpcExcel.SpcExcelArray(report_name,"PRF",app_path)
    excel_spr = SpcExcel.SpcExcelArray(report_name,"SPR",app_path)
    excel_rsm = SpcExcel.SpcExcelArray(report_name,"RSM",app_path)
    excel_teg = SpcExcel.SpcExcelArray(report_name,"TEG",app_path)
    

    #获得测试项目列表 [mec,stat,item]
    mec_now = ""
    stat_now = ""
    item_now = ""
    list_item = []
    
    for i in array_mulu.index:
        if array_mulu.loc[i][0] is not np.nan:
            mec_now = array_mulu.loc[i][0]
        if array_mulu.loc[i][1] is not np.nan:
            stat_now = array_mulu.loc[i][1]
        item_now = array_mulu.loc[i][2]
        list_item.append([str(mec_now),str(stat_now),str(item_now)])
    dict_var = {}
    #根据测试项目对表格进行拆分，形成各项目列表
    for i in range(len(list_item)):
        if list_item[i][0] == "CDC":
            dict_var["%s"%( "".join(list_item[i]))] = \
                                  excel_cdc.spcfilter(list_item[i][1],list_item[i][2])
        if list_item[i][0] == "PRF":
            dict_var["%s"%( "".join(list_item[i]))] = \
                                  excel_prf.spcfilter(list_item[i][1],list_item[i][2])
        if list_item[i][0] == "SPR":
            dict_var["%s"%( "".join(list_item[i]))] = \
                                  excel_spr.spcfilter(list_item[i][1],list_item[i][2])
        if list_item[i][0] == "RSM":
            dict_var["%s"%( "".join(list_item[i]))] = \
                                  excel_rsm.spcfilter(list_item[i][1],list_item[i][2])
        if list_item[i][0] == "TEG":
            dict_var["%s"%( "".join(list_item[i]))] = \
                                  excel_teg.spcfilter(list_item[i][1],list_item[i][2])
        logging.info("CDCorg" + str(excel_cdc.e_array.shape))
    for key,value in dict_var.items():
        logging.info(key + str(value.e_array.shape))
        logging.info(key + "point" + str(value.e_array_e_point.shape))
        logging.info(key + "ave" + str(value.e_array_e_ave.shape))
        logging.info(key + "all" + str(value.e_array_e_all.shape))

    
    excel_cdc.e_array2excel(dict_var)
    
def open_report(app_path,report_name):
    
    spc_excel_path = app_path + "SPC"+"\\"+ report_name
    xlapp = win32com.client.Dispatch('excel.application')
    xlapp.visible=1
    xlbook = xlapp.workbooks.open(spc_excel_path)
            
    
        
    

if __name__ == "__main__":
    #datefenxi("20181207.xls")
    app_path = r"\\172.22.100.52\武汉天马\面板厂\阵列部\PHOTO\全公司可读" +\
        r"\11.刘漫\00-过程管控\SPC管控"+"\\"
    open_report(app_path,"20180228.xlsm")
    
    
   
