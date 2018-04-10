#!/usr/bin/env python
#encoding: utf-8
import requests
import re
# 下面三行是编码转换的功能
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
f = open('C:\\Users\\Windsor\\Desktop\\TaoBaoList.txt')
lines = f.readlines()
f.close()
# print lines[17]
# a = lines[17].split(' ')
# for i in a:
#     print i
file_object = open('C:\\Users\\Windsor\\Desktop\\list.txt', 'w')

wordList = set([])
for line in lines:
    line = line.replace('/',' ')
    a = line.split(' ')
    for i in a:
        i.replace(' ','')
        if i.strip():
            # print i.strip()
            wordList.add(i.strip())

for i in wordList:
    file_object.write(i.strip() + '\n')
    print  i
file_object.close( )
