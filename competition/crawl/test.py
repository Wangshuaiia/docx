#coding=utf-8
import re
import sys
import chardet
reload(sys)
sys.setdefaultencoding('utf8')
# relink = r'.*"tag":"(.*)","weight"'
nid = r"\"nid\":\"(\d{12})"
Pattern = re.compile(nid)
# info = 'jsonp924({"tags":{"dimenSum":8,"innerTagCloudList":"","rateSum":2714,"structuredRateStatisticList":[],"tagClouds":[{"count":670,"id":"620","posi":true,"tag":"质量很好","weight":0},{"count":455,"id":"520","posi":true,"tag":"很划算","weight":0},{"count":335,"id":"1423","posi":true,"tag":"很舒服","weight":0},{"count":310,"id":"123","posi":true,"tag":"布料好","weight":0},{"count":307,"id":"223","posi":true,"tag":"码数很准","weight":0},{"count":249,"id":"1523","posi":true,"tag":"穿着效果好","weight":0},{"count":144,"id":"523","posi":true,"tag":"外形好看","weight":0},{"count":126,"id":"923","posi":true,"tag":"做工很赞","weight":0},{"count":73,"id":"223","posi":false,"tag":"尺寸有偏差","weight":0},{"count":45,"id":"923","posi":false,"tag":"做工一般","weight":0}],"userTagCloudList":""}})'
info = '"nid":"549411444912","category":"500101580000","pid":"000000000000","title":"性价比！！贴布绣飞行服夹克 '
cinfo = Pattern.findall(info)
print cinfo
# strlist = info.split('p4pTags')
# for i in strlist:
#     print i
#     cinfo = Pattern.findall(info)
#     if cinfo:
#         print cinfo[0].encode('utf-8')