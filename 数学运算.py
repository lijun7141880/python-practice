#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo 在用计算机编程解决问题的过程中，数学运算是很常用的。python自带了一些基本的数学运算方法
# todo python的数学运算模块叫做math，再用之前，你需要
import math

x = 4
y = 2
# todo math包里有两个常量：
math.pi
# todo 圆周率π：3.141592...

math.e
# todo 自然常数：2.718281...

# todo 数值运算：
print math.ceil(x)
# todo 对x向上取整，比如x=1.2，返回2.0（py3返回2）

print math.floor(x)
# todo 对x向下取整，比如x=1.2，返回1.0（py3返回1）

print math.pow(x, y)
# todo 指数运算，得到x的y次方

print math.log(x)
# todo 对数，默认基底为e。可以使用第二个参数，来改变对数的基底。比如math.log(100, 10)

print math.sqrt(x)
# todo 平方根

print math.fabs(x)
# todo 绝对值

# todo 三角函数:
try:
    print math.sin(x)
    print math.cos(x)
    print math.tan(x)
    print math.asin(x)
    print math.acos(x)
    print math.atan(x)
except:
    print '...'  # todo 注意：这里的x是以弧度为单位，所以计算角度的话，需要先换算

# todo 角度和弧度互换:
print math.degrees(x)
# todo 弧度转角度

print math.radians(x)
# todo 角度转弧度

# todo 练习 利用以上方法实现 (-b±√(b²-4ac))/2a 表达式
import math

def gongshi(a, b, c):
    print (-b + math.sqrt((math.pow(b, 2) - 4 * a * c))) / 2 * a
    print (-b - math.sqrt((math.pow(b, 2) - 4 * a * c))) / 2 * a
gongshi(1, 2, -1)
