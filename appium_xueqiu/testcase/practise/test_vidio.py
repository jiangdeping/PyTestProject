# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/28 14:45
import os
import shlex
import signal
import subprocess
from time import sleep
import time

def  test_screen():
    file_time=time.strftime("%Y%m%d%H%M%S")
    filepath=os.path.dirname(os.path.abspath(__file__))
    file_name=filepath+"\\Result_Screen\\"+file_time+".mp4"
    cmd=f'scrcpy --record {file_name}'
    subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
    sleep(3)
    kill_scrcpy="taskkill /IM scrcpy.exe" #结束进程
    os.system(kill_scrcpy)

    # os.kill(p.pid,signal.CTRL_C_EVENT)
    # p.send_signal(signal.CTRL_C_EVENT)