# -*- encoding: utf-8 -*-
"""
    Copyright (C) 2015 Jaehyun Ahn
    Weibo Crawler Module
    Author: Sogo
    Referred : https://github.com/KeithYue/weibo-keywords-crawler
            https://github.com/mcgrady164/Sina-Weibo-Crawler-/blob/master/SinaWeiboAPICrawler.py
            <httplib2>
            https://code.google.com/p/httplib2/wiki/Examples
            <logged on>
            http://www.weibo.com/u/5540518761/home?wvr=5
"""
import httplib2
import urllib

http = httplib2.Http('.cache')
# id: username id: password
# TRIAL: http://login.sina.com.cn/signup/signin.php?entry=sso
#        http://www.weibo.com/login.php
url = 'http://login.sina.com.cn/signup/signin.php?entry=sso'
body = {'username': '00821043197019', 'password': 'wn9889zn1'}
headers = {'Content-type': 'application/x-www-form-urlencoded'}

http.add_credentials('00821043197019', '--')
response, content = http.request(url, 'POST', headers=headers
                                 , body=urllib.parse.urlencode(body))

print ('COOKIE: ' + response['set-cookie'])
headers = {'Cookie': response['set-cookie']}

url = 'http://www.weibo.com/u/5540518761/home?wvr=5'
response, content = http.request(url, 'GET', headers=headers)


print (content)
f = open('test.html', 'w')
f.write(str(content))
f.close()