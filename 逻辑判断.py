#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo 一个逻辑表达式，其实最终是代表了一个bool类型的结果
# todo 1 < 3  这个就像当于是一个True的值
# todo 2 == 3  这个就是False
# todo 把它们作为判断条件放到if或者while的后面，就是根据他们的值来决定要不要执行。

# todo 习题
a = True
b = not a
print b #False
print not b #True
print a == b #False
print a != b #True
print a and b #False
print a or b #True
print 1<2 and b==True #False