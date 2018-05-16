import matplotlib.pyplot as plt
import re
class mapata(object):
    def __init__(self,file_path):
        self.job_speci = ''
        self.regin_num = 0
        self.job_param = ''
        self.reticle_part_num = ''
        self.regin_info = {}
        self.site_info = {}

        self.readfile(file_path)

    def readfile(self,file_path):
        iter_file = open(file_path)
        for text in iter_file.readlines():
            #a = re.split('[\s+]',text)
            if text[1:4] == 'HJS':
                self.job_speci = re.search(r'\d+',text).group()
                print(self.job_speci)
            elif text[1:4] == 'HR ':
                self.regin_num = re.search(r'\d+',text).group()
                print(self.regin_num)
            elif text[1:4] == 'HPF ':
                self.job_param = re.search(r'\d+',text).group()
                print(self.job_param)
            elif text[1:4] == 'WN ':
                self.reticle_part_num = re.search(r'\S+',text.split(':')[1]).group()
                print(self.reticle_part_num)
            elif text[1:4] == 'RL ':
                regin_ID = re.search(r'\d+',text).group()
                self.regin_info[regin_ID] = {}
            elif text[1:4] == 'RW ':
                self.regin_info[regin_ID]['RW'] = float(re.search(r'[-]*\d+.\d+',text).group())
            elif text[1:4] == 'RH ':
                self.regin_info[regin_ID]['RH'] = float(re.search(r'[-]*\d+.\d+',text).group())
            elif text[1:4] == 'RX ':
                self.regin_info[regin_ID]['RX'] = float(re.search(r'[-]*\d+.\d+',text).group())
            elif text[1:4] == 'RY ':
                self.regin_info[regin_ID]['RY'] = float(re.search(r'[-]*\d+.\d+',text).group())
            elif text[1:4] == 'ROX':
                self.regin_info[regin_ID]['ROX'] = float(re.search(r'[-]*\d+.\d+',text).group())
            elif text[1:4] == 'ROY':
                self.regin_info[regin_ID]['ROX'] = float(re.search(r'[-]*\d+.\d+',text).group())
            elif text[1:4] == 'RT ':
                self.regin_info[regin_ID]['RT'] = float(re.search(r'[-]*\d+.\d+',text).group())
            elif text[1:4] == 'RSX':
                self.regin_info[regin_ID]['RSX'] = float(re.search(r'[-]*\d+.\d+',text).group())
            elif text[1:4] == 'RSY':
                self.regin_info[regin_ID]['RSY'] = float(re.search(r'[-]*\d+.\d+',text).group())
            elif text[1:4] == 'ROR':
                self.regin_info[regin_ID]['ROR'] = float(re.search(r'[-]*\d+.\d+',text).group())
            elif text[1:4] == 'PL ':
                Pass_ID = re.search(r'\d+',text).group()
                self.site_info[Pass_ID] = {}
            elif text[1:4] == 'PT ':
                self.site_info[Pass_ID]['PT'] = re.search(r'\S.*',text.split(':')[1]).group()
            elif text[1:4] == 'PIW':
                self.site_info[Pass_ID]['PIW'] = float(re.search(r'[-]*\d+.\d+',text).group())
            elif text[1:4] == 'PIH':
                self.site_info[Pass_ID]['PIH'] = float(re.search(r'[-]*\d+.\d+',text).group())
            elif text[1:4] == 'PIX':
                self.site_info[Pass_ID]['PIX'] = float(re.search(r'[-]*\d+.\d+',text).group())
            elif text[1:4] == 'PIY':
                self.site_info[Pass_ID]['PIY'] = float(re.search(r'[-]*\d+.\d+',text).group())
            elif text[1:4] == 'SS ':
                Site_ID = re.search(r'\d+',text).group()
                self.site_info[Pass_ID][Site_ID] = {}
            elif text[1:4] == 'SX ':
                self.site_info[Pass_ID][Site_ID]['SX'] = float(re.search(r'[-]*\d+.\d+',text).group())
            elif text[1:4] == 'SY ':
                self.site_info[Pass_ID][Site_ID]['SY'] = float(re.search(r'[-]*\d+.\d+',text).group())
            elif text[1:4] == 'SOX':
                self.site_info[Pass_ID][Site_ID]['SOX'] = float(re.search(r'[-]*\d+.\d+',text).group())
            elif text[1:4] == 'SOY':
                self.site_info[Pass_ID][Site_ID]['SOY'] = float(re.search(r'[-]*\d+.\d+',text).group())



        pass            
            
     


if __name__ == '__main__':
    a = mapata(r'C:\Users\Administrator\Desktop\hkj\275_site_correction_map1')
    #a = oldata(r'C:\Users\Administrator\Desktop\hkj\新建文件夹\OL20180429175018.csv')

        
