#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
工具类
author:zhua
'''
import os
import subprocess
import time

adb = os.path.join(os.environ["ANDROID_HOME"], "platform-tools", "adb.exe")


# adb shell 命令
def shell(args):
    cmd = "%s shell %s" % (adb, str(args))
    print(cmd)
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


# 时间戳
def timestamp():
    return time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))

