#!/usr/bin/python
# -*- coding: utf-8 -*-
# todo 如果我们希望自己定义的函数里允许调用者提供一些参数，就把这些参数写在括号里，如果有多个参数，用逗号隔开
# todo 如：
def sayHello(someone):
   print someone + ' says Hello!'
sayHello('lijun')
# todo 或者
def plus(num1, num2):
   print num1+num2
plus(1,2)
# todo 或者也可以传入变量：
x = 3
y = 4
plus(x, y)
# todo 在这个函数被调用时，相当于做了num1=x, num2=y这么一件事。所以结果是输出了7。
# todo 参数在函数中相当于一个变量，而这个变量的值是在调用函数的时候被赋予的。在函数内部，你可以像过去使用变量一样使用它。
# todo 调用带参数的函数时，同样把需要传入的参数值放在括号中，用逗号隔开。要注意提供的参数值的数量和类型需要跟函数定义中的一致。如果这个函数不是你自己写的，你需要先了解它的参数类型，才能顺利调用它。