# coding:utf-8
import random
import re
import sys
import time
import datetime

reload(sys)
a = 0
for i in range(1,10):
    time.sleep(1)
    print i
    now = datetime.datetime.now()
    print now.strftime('%Y-%m-%d %H:%M:%S')
