# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
accept_encoding = 'gzip, deflate, br'
accept_language = 'zh-CN,zh;q=0.9'
cache_control = 'max-age=0'
connection = 'keep-alive'
host = 'www.qiushibaike.com'

headers = {'User-Agent': user_agent, 'Accept': accept, 'Accept-Encoding': accept_encoding,
           'Accept-Language': accept_language, 'Cache-Control': cache_control,
           'Connection': connection, 'Host': host}
headers = {'User-Agent': user_agent}
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    # print response.read()
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print "e.code: ", e.code
    if hasattr(e, "reason"):
        print "e.reason: ", e.reason

content = response.read().decode('utf-8')
pattern = re.compile('<div.*?author.*?">.*?<div.*?content">(.*?)</div>.*?<div class="stats.*?class="number">(.*?)</i>', re.S)
items = re.findall(pattern, content)
for item in items:
    # haveImg = re.search("img",item[3])
    # if not haveImg:
    print item[0]


