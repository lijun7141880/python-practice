#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo 元组（tuple）也是一种序列，和list类似，只是元组中的元素在创建之后就不能被修改。

# todo 如：
postion = (1, 2)
geeks = ('Sheldon', 'Leonard', 'Rajesh', 'Howard')
# todo 都是元组的实例。它有和list同样的索引、切片、遍历等操作：
print postion[0] #1
for g in geeks:
    print g  # Sheldon Leonard Rajesh Howard
print geeks[1:3]  # ('Leonard', 'Rajesh')

# todo 其实我们之前一直在用元组，就是在print语句中：
print '%s is %d years old' % ('Mike', 23)  # ('Mike', 23)就是一个元组。这是元组最常见的用处。

# todo 再来看一下元组作为函数返回值的例子：
def get_pos(n):
    return (n/2, n*2)

# todo 得到这个函数的返回值有两种形式，一种是根据返回值元组中元素的个数提供变量：
x, y = get_pos(50)
print x  # 25
print y  # 100

# todo 还有一种方法是用一个变量记录返回的元组：
pos = get_pos(50)
print pos[0]  # 25
print pos[1]  # 100