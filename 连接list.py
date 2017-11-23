#!/usr/bin/python
# -*- coding: utf-8 -*-
# todo split是把一个字符串分割成很多字符串组成的list，而join则是把一个list中的所有字符串连接成一个字符串。
# todo join的格式有些奇怪，它不是list的方法，而是字符串的方法。首先你需要有一个字符串作为list中所有元素的连接符，然后再调用这个连接符的join方法，join的参数是被连接的list：
s = ';'
li = ['apple', 'pear', 'orange']
fruit = s.join(li)
print fruit
# todo 得到结果'apple;pear;orange'。
# todo 从结果可以看到，分号把list中的几个字符串都连接了起来。

print ';'.join(['apple', 'pear', 'orange']) #得到同样的结果。

# todo 用来连接的字符串可以是多个字符，也可以是一个空串：
print ''.join(['hello', 'world'])
# todo 得到'helloworld'，字符串被无缝连接在一起。
