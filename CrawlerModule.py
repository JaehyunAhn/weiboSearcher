# -*- encoding: utf-8 -*-
"""
    Copyright (C) 2015 Jaehyun Ahn
    Weibo Crawler Module
    Author: Sogo
"""
import urllib
import urllib2

f = open('test.html', 'w')

# login form이 잘못되었음
url = 'http://www.weibo.com/login.php'
login_form = {'id': '00821043197019', 'pw': 'wn9889zn1'}
login_req = urllib.urlencode(login_form)
# Request
request = urllib2.Request(url, login_req)
response = urllib2.urlopen(request)
cookie = response.headers.get('Set-Cookie')
data = response.read()
f.write(data)

url = 'http://s.weibo.com/wb/exo'
request = urllib2.Request(url)
request.add_header('cookie', cookie)
response = urllib2.urlopen(request)


# data = response.read()
# f.write(data)
f.close()