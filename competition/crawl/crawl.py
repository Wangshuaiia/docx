#coding=utf-8
import requests as rq
import requests
import random
import re
import time
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# url='http://rate.tmall.com/list_detail_rate.htm?itemId=41464129793&sellerId=1652490016&currentPage=1'
# url = 'https://rate.tmall.com/listTagClouds.htm?itemId=547705806687&isAll=true&isInner=true&t=1508372644153&_ksTS=1508372644153_923&callback=jsonp924'
# url = 'https://rate.tmall.com/listTagClouds.htm?itemId=547705806687&isAll=true&isInner=true&t=1508372644153&callback=jsonp924'
user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]
f = open('C:\\Users\\Windsor\\Desktop\\ipList.txt')
IPlines = f.readlines()
f.close()

# hea = {
#       'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}
f = open('C:\\Users\\Windsor\\Desktop\\nid.txt')
list = f.readlines()
f.close()
Tags = []
file_object = open('C:\\Users\\Windsor\\Desktop\\Tags.txt', 'a')
errorTime = open('C:\\Users\\Windsor\\Desktop\\errorTime.txt', 'a')
for i in list:
    url = 'https://rate.tmall.com/listTagClouds.htm?itemId={}&isAll=true'.format(i)
    print url
    hea = random.choice(user_agent_list)  ##从self.user_agent_list中随机取出一个字符串
    header = {'User-Agent':hea}
    IP = ''.join(str(random.choice(IPlines)).strip())  ##将从self.iplist中获取的字符串处理成我们需要的格式
    proxy = {'http': IP}  ##构造成一个代理
    try:
        myweb = requests.get(url, headers=header, proxies=proxy)  ##使用代理获取response
        # myweb = requests.get(url, headers=hea)
        # myweb = rq.get(url, headers=hea)
        # myweb.encoding = 'utf-8'
        relink = r'\"tag\":\"(.{1,35})\","weight"'
        Pattern = re.compile(relink)
        info = str(myweb.text)
        # strlist = info.split('}')
        # for j in strlist:
        cinfo = Pattern.findall(info)
        print cinfo
        for j in cinfo:
            if cinfo:
                print j
                # print cinfo[0].encode('utf-8')
                Tags.append(j.encode('utf-8'))
                file_object = open('C:\\Users\\Windsor\\Desktop\\Tags.txt', 'a')
                file_object.write(j.strip() + '\n')
                file_object.close()
    except BaseException:
        now = datetime.datetime.now()
        print "有错误的nid: "+str(i)+str(now.strftime('%Y-%m-%d %H:%M:%S'))
        errorTime = open('C:\\Users\\Windsor\\Desktop\\errorTime.txt', 'a')
        errorTime.write(str(i)+str(now.strftime('%Y-%m-%d %H:%M:%S'))+'\n')
        errorTime.close()
        time.sleep(5)

print "----------------end----------------------------------------------------"
print len(Tags)
errorTime.close()
file_object.close()
