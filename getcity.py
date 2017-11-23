#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo 天气网并没有直接给出所有城市代码的对应关系，而是给了3个接口：
# todo 1. http://m.weather.com.cn/data5/city.xml     获取所有省/直辖市的编号，如“01|北京,02|上海,03|天津”
# todo 2. http://m.weather.com.cn/data5/city省编号.xml     获取二级地区编号，如江苏是：city19.xml
# todo 3. http://m.weather.com.cn/data5/city二级编号.xml     获取三级编号，如南京是：city1901.xml

import urllib2

url1 = 'http://m.weather.com.cn/data5/city.xml'
content1 = urllib2.urlopen(url1).read()
provinces = content1.split(',')
result = 'city = {\n'
url = 'http://m.weather.com.cn/data3/city%s.xml'
for p in provinces:
    p_code = p.split('|')[0]
    url2 = url % p_code
    content2 = urllib2.urlopen(url2).read()
    cities = content2.split(',')
    for c in cities[:3]:
        c_code = c.split('|')[0]
        url3 = url % c_code
        content3 = urllib2.urlopen(url3).read()
        districts = content3.split(',')
        for d in districts:
            d_pair = d.split('|')
            d_code = d_pair[0]
            name = d_pair[1]
            url4 = url % d_code
            content4 = urllib2.urlopen(url4).read()
            code = content4.split('|')[1]
            line = "    '%s': '%s',\n" % (name, code)
            result += line
            print  name + ':' + code
result += '}'
f = file('data/city2.py', 'w')
f.write(result)
f.close()
