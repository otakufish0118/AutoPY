import subprocess
import time
import cv2 as cv
import os

os.system("cls")
dirpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
imname = "im"

t1 = time.time()

scrcap = "{0}\\nox_adb.exe shell screencap -p /sdcard/{1}.png".format(dirpath, imname)
print("指令1 抓圖:{0}".format(scrcap))
subprocess.call(scrcap)
time.sleep(3)
impull = "{0}\\nox_adb.exe pull /sdcard/{1}.png".format(dirpath, imname)
print("指令2 存檔:{0}".format(impull))
subprocess.call(impull)

im = cv.imread("{0}\\py\\im.png".format(dirpath))
t2 = time.time()
print("總耗時{0}秒".format(round(t2-t1, 2)))
try:
    if int(im.shape[0]) % 9 != 0 or int(im.shape[1] % 16) != 0:
        print("你螢幕解析度是{0} x {1}".format(
            int(im.shape[1] % 9), int(im.shape[0])))
    elif im.shape[0] != 1280 and im.shape[1] != 720:
        print("模擬器解析度原圖為: {0} x {1}".format(
            im.shape[1], im.shape[0]))
except:
    print("你模擬器截取出來的圖片爆炸了,有兩個建議選項,一個重灌電腦一個重灌模擬器一個想辦法自己解決")
