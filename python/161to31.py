import os
import shutil
import time

def f161to31():
    
    path161 = r'\\172.27.110.161\micresult' + '\\'
    target = r'\\172.22.100.52\***\CDC100'
    timeStruct1 = time.localtime(time.time())
    timeStruct2 = time.localtime(time.time()-24*60*60)

    time1 =time.strftime('%Y%m%d',timeStruct1)
    time2 = time.strftime('%Y%m%d',timeStruct2)

    for root,dirs,files in os.walk(path161 + time1):
        for file1 in files:
            if file1[-3:] == 'csv':
                if os.path.exists(target + root[26:]):
                    if os.path.exists(target + os.path.join(root, file1)[26:]):
                        pass
                    else:
                        shutil.copyfile(os.path.join(root, file1),target + os.path.join(root, file1)[26:])
                        print(os.path.join(root, file1))
                else:
                    os.makedirs(target + root[26:])

    for root,dirs,files in os.walk(path161 + time2):
        for file1 in files:
            if file1[-3:] == 'csv':
                if os.path.exists(target + root[26:]):
                    if os.path.exists(target + os.path.join(root, file1)[26:]):
                        pass
                    else:
                        shutil.copyfile(os.path.join(root, file1),target + os.path.join(root, file1)[26:])
                        print(os.path.join(root, file1))
                else:
                    os.makedirs(target + root[26:])
def f161to31pic():
    
    path161 = r'\\172.27.110.161\image_auto_save' + '\\'
    #path161 = r'M:\调查中事项' + '\\'
    target = r'\\172.22.100.52\**\CDC100image'



    for dir1 in os.listdir(path161):
        if os.path.isdir(os.path.join(path161, dir1)):
            if dir1 != 'auto1_temp_image_save_folder':
                if (time.time() - os.stat(os.path.join(path161, dir1)).st_mtime) < 3600:
                    if os.path.exists(os.path.join(target, dir1)):
                        for dir2 in os.listdir(os.path.join(path161, dir1)):
                            if os.path.isdir(os.path.join(os.path.join(path161, dir1), dir2)):
                                if (time.time() - os.stat(os.path.join(os.path.join(path161, dir1), dir2)).st_mtime) < 3600:
                                    target1 = os.path.join(os.path.join(target , dir1) , dir2)
                                    source1 = os.path.join(os.path.join(path161 , dir1) , dir2)
                                    if os.path.exists(target1):
                                        for file1 in os.listdir(source1):
                                            if file1[-3:] == 'jpg':
                                                if os.path.exists(os.path.join(target1, file1)):
                                                     pass
                                                else:
                                                    shutil.copyfile(os.path.join(source1 , file1),os.path.join(target1, file1))
                                                    print(os.path.join(source1 , file1))
                                    else:
                                        os.makedirs(target1)

                        
                    else:
                        os.makedirs(os.path.join(target, dir1))
                    
                    
                        

        
def f162to31pic():
    
    path161 = r'\\172.27.110.162\image_auto_save' + '\\'
    #path161 = r'M:\调查中事项' + '\\'
    target = r'\\172.22.100.52\**\CDC200image'



    for dir1 in os.listdir(path161):
        if os.path.isdir(os.path.join(path161, dir1)):
            if dir1 != 'auto1_temp_image_save_folder':
                if (time.time() - os.stat(os.path.join(path161, dir1)).st_mtime) < 7200:
                    if os.path.exists(os.path.join(target, dir1)):
                        for dir2 in os.listdir(os.path.join(path161, dir1)):
                            if os.path.isdir(os.path.join(os.path.join(path161, dir1), dir2)):
                                if (time.time() - os.stat(os.path.join(os.path.join(path161, dir1), dir2)).st_mtime) < 7200:
                                    target1 = os.path.join(os.path.join(target , dir1) , dir2)
                                    source1 = os.path.join(os.path.join(path161 , dir1) , dir2)
                                    if os.path.exists(target1):
                                        for file1 in os.listdir(source1):
                                            if file1[-3:] == 'jpg':
                                                if os.path.exists(os.path.join(target1, file1)):
                                                     pass
                                                else:
                                                    shutil.copyfile(os.path.join(source1 , file1),os.path.join(target1, file1))
                                                    print(os.path.join(source1 , file1))
                                    else:
                                        os.makedirs(target1)

                        
                    else:
                        os.makedirs(os.path.join(target, dir1))
                    
                    
                        

    
def f162to31():
    path162 = r'\\172.27.110.162\micresult' + '\\'
    target = r'\\172.22.100.52\**\CDC200'
    timeStruct1 = time.localtime(time.time())
    timeStruct2 = time.localtime(time.time()-24*60*60)

    time1 =time.strftime('%Y%m%d',timeStruct1)
    time2 = time.strftime('%Y%m%d',timeStruct2)

    for root,dirs,files in os.walk(path162 + time1):
        for file1 in files:
            if file1[-3:] == 'csv':
                if os.path.exists(target + root[26:]):
                    if os.path.exists(target + os.path.join(root, file1)[26:]):
                        pass
                    else:
                        shutil.copyfile(os.path.join(root, file1),target + os.path.join(root, file1)[26:])
                        print(os.path.join(root, file1))
                else:
                    os.makedirs(target + root[26:])

    for root,dirs,files in os.walk(path162 + time2):
        for file1 in files:
            if file1[-3:] == 'csv':
                if os.path.exists(target + root[26:]):
                    if os.path.exists(target + os.path.join(root, file1)[26:]):
                        pass
                    else:
                        shutil.copyfile(os.path.join(root, file1),target + os.path.join(root, file1)[26:])
                        print(os.path.join(root, file1))
                else:
                    os.makedirs(target + root[26:])
if __name__ == '__main__':
    while True:
        print(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())))
        
        f161to31()
        f162to31()
        f161to31pic()
        f162to31pic()
        for i in range(30):
            time.sleep(1)
