#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo 看下面这段代码：
a = "heaven"
b = "hell"
c = True and a or b
print c  # heaven  表达式从左往右运算，1和"heaven"做and的结果是"heaven"，再与"hell"做or的结果是"heaven"
d = False and a or b
print d  # hell  0和"heaven"做and的结果是0，再与"hell"做or的结果是"hell"。

# todo 你只需记住，在一个bool and a or b语句中，当bool条件为真时，结果是a；当bool条件为假时，结果是b。
# todo 原本需要一个if-else语句表述的逻辑：
if a > 0:
    print "big"
else:
    print "small"

# todo 就可以直接写成：
print (a > 0) and "big" or "small"

# todo 但是当a本身是个假值（如0，""）时，结果就不会像你期望的那样。
# todo 比如：
a = ""
b = "hell"
c = True and a or b
print c # 得到的结果不是""而是"hell"。因为""和"hell"做or的结果是"hell"。

# todo 所以，and-or真正的技巧在于，确保a的值不会为假。最常用的方式是使 a 成为 [a] 、 b 成为 [b]，然后使用返回值列表的第一个元素：
a = ""
b = "hell"
c = (True and [a] or [b])[0]
print c
# todo 由于[a]是一个非空列表，所以它决不会为假。即使a是0或者''或者其它假值，列表[a]也为真，因为它有一个元素。