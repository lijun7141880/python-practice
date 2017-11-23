#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo 实现这样一个小程序，你输入一个城市的名称，就会告诉你这个城市现在的天气情况。
# todo 之所以能知道一个城市的天气，是因为用了中国天气网（www.weather.com.cn）提供的天气查询接口。
# todo http://www.weather.com.cn/data/cityinfo/101010100.html

# todo 在这个程序中，我们要用到两个新模块：
# todo 1. urllib2   用来发送网络请求，获取数据
# todo 2. json   用来解析获得的数据

# todo 天气网并没有直接给出所有城市代码的对应关系，而是给了3个接口：
# todo 1. http://m.weather.com.cn/data5/city.xml     获取所有省/直辖市的编号，如“01|北京,02|上海,03|天津”
# todo 2. http://m.weather.com.cn/data5/city省编号.xml     获取二级地区编号，如江苏是：city19.xml
# todo 3. http://m.weather.com.cn/data5/city二级编号.xml     获取三级编号，如南京是：city1901.xml

# todo 首先，抓取省份的列表：
import urllib2
url1 = 'http://m.weather.com.cn/data5/city.xml'
content1 = urllib2.urlopen(url1).read()
provinces = content1.split(',')

# todo 对于每个省，抓取城市列表：
url = 'http://m.weather.com.cn/data3/city%s.xml'
for p in provinces:
   p_code = p.split('|')[0]
   url2 = url % p_code
   content2 = urllib2.urlopen(url2).read()
   cities = content2.split(',')

# todo 再对于每个城市，抓取地区列表：
for c in cities[:3]:
   c_code = c.split('|')[0]
   url3 = url % c_code
   content3 = urllib2.urlopen(url3).read()
   districts = content3.split(',')


# todo 最后，对于每个地区，我们把它的名字记录下来，然后再发送一次请求，得到它的最终代码：
for d in districts:
   d_pair = d.split('|')
   d_code = d_pair[0]
   name = d_pair[1]
   url4 = url % d_code
   content4 = urllib2.urlopen(url4).read()
   code = content4.split('|')[1]

# todo name和code就是我们最终要得到的城市代码信息。它们格式化到字符串中，最终保存在文件里：
line = "    '%s': '%s',\n" % (name, code)
result += line

# todo 同时你也可以输出它们，以便在抓取的过程中查看进度：
print  name + ':' + code

# todo urllib2是python中一个用来获取网络资源的模块。
import urllib2 #引入rullib2模块
import json
# web = urllib2.urlopen('http://www.baidu.com') #使用urllib2模块的urlopen方法，打开一个网址
# content = web.read() #读取网址的内容
# print content #把内容输出到控制台

from city import city
cityname = raw_input('你想查哪个城市的天气？\n')
citycode = city.get(cityname)
if citycode:
    try:
        url = ('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
        content = urllib2.urlopen(url).read()
        # print content
        data = json.loads(content)
        # print data
        # print type(content)
        # print type(data)
        result = data['weatherinfo']
        str_temp = ('%s\n%s--%s') % (result['weather'], result['temp1'], result['temp2'])
        print str_temp
    except:
        print '查询失败'
else:
    print '没有找到该城市'