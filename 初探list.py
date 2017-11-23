#!/usr/bin/python
# -*- coding: utf-8 -*-
# todo list，中文可以翻译成列表，是用来处理一组有序项目的数据结构。
for i in range(1, 10):
    print i
print range(1, 10)
# todo [1, 2, 3, 4, 5, 6, 7, 8, 9] 这就是一个list。它由range产生。
# todo py3不再直接返回列表，而是一个range对象，但不影响循环遍历。
l = range(1, 10)
for i in l:
    print i
# todo for循环做的事情其实就是遍历一个列表中的每一项，每次循环都把当前项赋值给一个变量（这里是i），直到列表结束。
l = [1, 1, 2, 3, 5, 8, 13]
print l
# todo 列表中的元素也可以是别的类型
l = ['meat', 'egg', 'fish', 'milk']
for i in l:
    print i
# todo 甚至是不同类型的混合
l = [365, 'everyday', 0.618, True]
for i in l:
    print i
