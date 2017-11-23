#!/usr/bin/python
# -*- coding: utf-8 -*-
# todo 变量命名规则
# todo 第一个字符必须是字母或者下划线“_”
# todo 剩下的部分可以是字母、下划线“_”或数字（0-9）
# todo 变量名称是对大小写敏感的，myname和myName不是同一个变量。

# todo 几个有效的栗子：
# todo    i
# todo   __my_name
# todo   name_23
# todo   a1b2_c3

# todo 几个坏掉的栗子（想一下为什么不对）：
# todo    2things  不能以数字开头
# todo    this is spaced out  不能有空格
# todo   my-name  不能有横杠

# todo python中运算的顺序是，先把“=”右边的结果算出了，再赋值给左边的变量。

# todo 利用变量、循环、累加，可以写一个程序
# todo 1+2+3+...+100=?
# todo 从1加到100等于多少？

x = 1
sum = 0
while x < 101:
    sum += x
    x += 1
print sum


