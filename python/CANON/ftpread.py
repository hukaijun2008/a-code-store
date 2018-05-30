import ftplib
import time
#CANON PHT100

def ftpcopy(machine):
    if machine == 'A1PHT100':
        host = '172.27.110.94'
    elif machine == 'A1PHT300':
        host = '172.27.110.98'
    elif machine == 'A1PHT500':
        host = '172.27.110.102'
    else:
        return 'link error'

    username = 'canon'

    password = 'mpa'
    flag = '0'
    try:

        f = ftplib.FTP(host)
        
        f.login(username, password)
        flag = '1'
        f.cwd('./log/monitor/')
        
        file = 'ADC.log'

        file_local = r'\\172.22.100.52\武汉天马\面板厂\阵列部\PHOTO\全公司可读\12.胡凯军\计测值' + '\\' + machine + '.log'

        fp = open(file_local, 'wb')
        flag = '2'
        bufsize = 1024

        f.retrbinary('RETR %s' % file, fp.write, bufsize)
        flag = '3'
        fp.close
        
        f.quit()
    except:
        return 'file error' + flag
    return 'ok'

if __name__ == '__main__':
    while True:
        print(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())))
        anstext = ftpcopy('A1PHT100')
        print(anstext)
        anstext = ftpcopy('A1PHT300')
        print(anstext)
        anstext = ftpcopy('A1PHT500')
        print(anstext)
        for i in range(60):
            time.sleep(1)
