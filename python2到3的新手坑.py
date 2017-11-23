#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo 1.print
# todo 在版本2的使用方法是：
print 'this is version 2'

# todo 也可以是
print('this is version 2')

# todo 但到了3，就只能加上括号，像一个函数一样来使用 print：
print('this is version 3')

# todo 版本2里不换行输出是加上逗号：
print '*',

# todo 到了3里就要改成：
# todo print('*', end=' ')

# todo 2.input
# todo 2里面有两个用来从命令行接受输入的函数：input 和 raw_input。

value = input()
# todo input 接收的是一个值或变量，也就是说，你如果输 123，程序接收到的就是整数 123，你输 True，就是 bool 值 True。如果你输了 abc，程序会认为这是一个叫做 abc 的变量，而假如你没有定义过这个变量，就会报错。
# todo 所以，当你想用 input 得到一段文字的话，必须把文字写在引号 "" 或 '' 中。

text = raw_input()
# todo raw_input 接收的则是你输入的字符串，而不管你输的是什么内容。如果你直接拿 raw_input 得到的“数字”去比较大小，则会得到奇怪的结果。

# todo 在版本3里，为了减少混乱，这两种输入方式被合并了。它接收你输入的字符串，不管你输的是什么。
# todo 那么在3里，如何像2一样得到用户输入的一个值呢？方法是 eval()：
# todo value = eval(input())
# todo 或者，如果你只是需要一个整数值，也可以：
# todo value = int(input())

# todo 除了一开始越到的这两个坑外，还有其他一些可能遇到的变动，这里以3与2相比的差异来说：

# todo 打开文件不再支持 file 方法，只能用 open
# todo range不再返回列表，而是一个可迭代的range对象
# todo 除法 / 不再是整除，而是得到浮点数，整除需要用双斜杠 //
# todo urllib和urllib2合并成了urllib，常用的urllib2.urlopen()变成了urllib.request.urlopen()
# todo 字符串及编码相关有大变动，简单来说就是原来的str变成了新的bytes，原来的unicode变成了新的str。