#!/usr/bin/python
# -*- coding: utf-8 -*-
# todo 之前我们用过函数，比如：
def hello(name):
   print 'hello ' + name
hello('world') #程序就会输出  hello world

# todo 如果很多时候，我们都是用world来调用这个函数，少数情况才会去改参数。那么，我们就可以给这个函数一个默认参数：
def hello(name = 'world'): #当你没有提供参数值时，这个参数就会使用默认值；如果你提供了，就用你给的。
   print 'hello ' + name
hello() #就可以输出  hello world

# todo 同样你也可以指定参数：
hello('python') #输出  hello python

# todo 注意，当函数有多个参数时，如果你想给部分参数提供默认参数，那么这些参数必须在参数的末尾。比如：
# def func(a, b=5) #是正确的
# def func(a=5, b) #就会出错
