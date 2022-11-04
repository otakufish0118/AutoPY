import os.path
import subprocess
import time

#class adbkit(object):
#    def __init__(self) -> None:
#        self.path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dirpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
killserver = "{0}\\nox_adb.exe kill-server".format(dirpath)
startserver = "{0}\\nox_adb.exe start-server".format(dirpath)
chkdevices = "{0}\\nox_adb.exe devices".format(dirpath)

subprocess.call(killserver)
subprocess.call(startserver)
time.sleep(10)
subprocess.call(chkdevices)

#    def debug_get(self):


