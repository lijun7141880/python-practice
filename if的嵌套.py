#!/usr/bin/python
# -*- coding: utf-8 -*-
# todo 和for循环一样，if也可以嵌套使用，即在一个if/elif/else的内部，再使用if。这有点类似于电路的串联
# todo if 条件1:
# todo    if 条件2:
# todo        语句1
# todo    else:
# todo        语句2
# todo else:
# todo    if 条件2:
# todo        语句3
# todo    else:
# todo        语句4
# todo 在上面这个两层if的结构中，当
# todo 条件1为True，条件2为True时，
# todo 执行语句1；
# todo 条件1为True，条件2为False时，
# todo 执行语句2；
# todo 条件1为False，条件2为True时，
# todo 执行语句3；
# todo 条件1为False，条件2为False时，
# todo 执行语句4。

# todo 判断（x，y）这个坐标在第几象限。
from random import randint
x = randint(-10, 10)
y = randint(-10, 10)
if x >= 0:
    if y >= 0:
        print 1
    else:
        print 4
else:
    if y >= 0:
        print 2
    else:
        print 3
