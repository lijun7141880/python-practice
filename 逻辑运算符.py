#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo 逻辑判断在编程中是非常重要的。大量的复杂程序在根本上都是建立在“真”与“假”的基本逻辑之上。而bool所表示的就是这种最单纯最本质的True/False，真与假，是与非

# todo 通过用“>”“<”来比较两个数值，我们就得到了一个boolean值。这个bool值的真假取决于比较的结果
# todo a = 1 < 3
# todo print a
# todo b = 1
# todo c = 3
# todo print b > c

# todo “>”“<”在编程语言中被成为逻辑运算符，常用的逻辑运算符包括：
# todo >：大于
# todo <：小于
# todo >=：大于等于
# todo <=：小于等于
# todo ==：等于。比较两个值是否相等。之所以用两个等号，是为了和变量赋值区分开来。
# todo !=：不等与
# todo not：逻辑“非”。如果x为True，则not x为False
# todo and：逻辑“与”。如果x为True，且y为True，则x and y为True
# todo or：逻辑“或”。如果x、y中至少有一个为True，则x or y为True

num = 10
print 'Guess what I think?'
answer = int(input())

result = answer<num
print 'too small?'
print result

result = answer>num
print 'too big?'
print result

result = answer==num
print 'equal?'
print result