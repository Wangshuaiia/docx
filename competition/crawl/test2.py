#!/usr/bin/env python
#encoding: utf-8
import requests
import re
# 下面三行是编码转换的功能
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# hea是我们自己构造的一个字典，里面保存了user-agent。
# 让目标网站误以为本程序是浏览器，并非爬虫。
# 从网站的Requests Header中获取。【审查元素】
f = open('C:\\Users\\Windsor\\Desktop\\list.txt')
lines = f.readlines()
f.close()
hea = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}
nid = r"\"nid\":\"(\d{12})"
Pattern = re.compile(nid)
Alllist = []
file_object = open('C:\\Users\\Windsor\\Desktop\\nid.txt', 'w')
for i in lines:
      url = 'https://s.taobao.com/search?q='+i
      html = requests.get(url, headers=hea)
      html.encoding = 'utf-8'  # 这一行是将编码转为utf-8否则中文会显示乱码。
      list = Pattern.findall(str(html.text))
      for i in list:
            file_object.write(i.strip() + '\n')
      # print  list
      Alllist+=list
print Alllist
file_object.close( )
# print str(html.text)
# strlist = str(html.text).split('"nid":')
# for i in strlist:
#       print "------------------------------------------------"
#       print  "======================================================="
#       print i
# print len(strlist)
