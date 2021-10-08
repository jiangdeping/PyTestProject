# -*- coding: utf-8 -*-
# Author:jiang
# 2021/9/28 14:44
import os
import subprocess
import time
import pytest


@pytest.fixture(scope="class",autouse=True)
def record():
    file_time = time.strftime("%Y%m%d%H%M%S")
    filepath = os.path.dirname(os.path.abspath(__file__))
    file_name = filepath + "\\Result_Screen\\" + file_time + ".mp4"
    cmd = f'scrcpy --record {file_name}'
    subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

    yield
    kill_scrcpy = "taskkill /IM scrcpy.exe"  # 结束进程
    os.system(kill_scrcpy)
