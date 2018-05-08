import pyautogui
import logging
import time
import os
logging.basicConfig(level=logging.DEBUG,format="%(asctime)s - %(levelname)s - %(message)s")
StepFile = open("data.txt")
StepData = StepFile.readlines()
for i in range(len(StepData)):
    if i == len(StepData)-1:
        OneStep = str.split(StepData[i],",")
    else:
        OneStep = str.split(StepData[i][:-1],",")
    logging.debug("OneStep is :" + ",".join(OneStep))
    if OneStep[0] == "Move":
        pyautogui.moveTo(int(OneStep[1]),int(OneStep[2]),float(OneStep[3]))
    elif OneStep[0] == "LeftClick":
        pyautogui.click(int(OneStep[1]),int(OneStep[2]))
    elif OneStep[0] == "LeftDouble":
        pyautogui.doubleClick(int(OneStep[1]),int(OneStep[2]))
    elif OneStep[0] == "Sleep":
        time.sleep(int(OneStep[1]))
    elif OneStep[0] == "RightClick":
        pyautogui.click(int(OneStep[1]),int(OneStep[2]),button="right")
    elif OneStep[0] == "Drag":
        pyautogui.moveTo(int(OneStep[1]),int(OneStep[2]))
        pyautogui.dragTo(int(OneStep[3]),int(OneStep[4]),float(OneStep[5]))
    elif OneStep[0] == "PatternMatch":
        flag = pyautogui.locateOnScreen(OneStep[1])
        if flag is None:
            print(OneStep[1]+"未匹配")
        else:
            pyautogui.moveTo(pyautogui.center(flag))
    elif OneStep[0] == "KeyIn":
        pyautogui.typewrite(OneStep[1],float(OneStep[2]))
    elif OneStep[0] == "HotKey":
        pyautogui.hotkey(OneStep[1],OneStep[2])