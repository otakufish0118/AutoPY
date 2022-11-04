import os
import subprocess
from campare import compare

adb_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
adb_cmd = "{0}\\nox_adb.exe devices".format(adb_path)

devices = subprocess.Popen(adb_cmd, stdout=subprocess.PIPE).stdout.read().decode("utf-8")
lists = devices.split("\n")
devices_name = []
for item in lists:
    if(item.strip() == ""):
        continue
    elif(item.startswith("List of")):
        continue
    else:
        devices_name.append(item.split("\t")[0])

i = 1
for deviceID in devices_name:
    port = deviceID.split(":")[1]
    print("{0}:{1}".format(i, port))
    i += 1

print("共有{0}組已連線設備".format(i - 1))
choose_port = input("選擇使用的port: ")
print("已選擇使用port是{0}的設備".format(devices_name[int(choose_port) - 1]))
choose_device = devices_name[int(choose_port) - 1]

adb_cap_cmd = "{0}\\nox_adb.exe -s {1} shell screencap -p /sdcard/cap.png".format(adb_path, choose_device)
adb_move_cmd = "{0}\\nox_adb.exe -s {1} pull /sdcard/cap.png".format(adb_path, choose_device)

subprocess.call(adb_cap_cmd)
subprocess.call(adb_move_cmd)

compare()
