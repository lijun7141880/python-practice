#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo python的几种最基本的数据类型:
# todo 字符串
# todo 整数
# todo 小数 （浮点数）
# todo bool类型
# todo python在定义一个变量时不需要给它限定类型。变量会根据赋给它的值，自动决定它的类型。你也可以在程序中，改变它的值，于是也就改变了它的类型。
a = 1
print a
a = 'hello'
print a
a = True
print a
# todo 变量a先后成为了整数、字符串、bool类型。

# todo 虽然类型可以随意改变，但当你对一个特定类型的变量进行操作时，如果这个操作与它的数据类型不匹配，就会产生错误。
# todo print ‘Hello’+1 #程序运行时会报错。因为字符串和整数不能相加
# todo print ‘hello%d’ % '123' #%d需要的是一个整数，而'123'是字符串

# todo 这种情况下，python提供了一些方法对数值进行类型转换：
# todo int(x) #把x转换成整数
# todo float(x) #把x转换成浮点数
# todo str(x) #把x转换成字符串
# todo bool(x) #把x转换成bool值

# todo 并不是所有的值都能做类型转换，比如int('abc')同样会报错，python没办法把它转成一个整数。

# todo 试试以下结果的值
print bool(-123) #True
print bool(0) #False
print bool('abc') #True
print bool('False') #True
print bool('') #False