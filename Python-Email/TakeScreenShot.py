#!/usr/bin/env python3

import pyautogui
import getpass
import time
import os

def TakeScreenShot():
    current_user = getpass.getuser()
    time_stamp = time.ctime()
    time_stamp = time_stamp.replace(' ','_')
    time_stamp = time_stamp.replace(':','_')
    file_name  = "screen_shot_"+time_stamp+'.png'
    image_path = "C:\\Users\\"+current_user+"\\Desktop\\"+file_name
    screenshot = pyautogui.screenshot()
    screenshot.save(image_path)

TakeScreenShot()
