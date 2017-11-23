#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo 1.读错误信息
# todo 例子
import random
a = 0
for i in range(5):
    b = random.choice(range(5))
    a += i / b
print a
# todo 这个程序中，i从0循环到4，每次循环中，b是0到4中的一个随机数。把i/b的结果累加到a上，最后输出结果。
# todo 运行这段程序，有时候会输出结果，有时候却跳出错误信息：
# todo Traceback (most recent call last):
# todo   File "E:/ѧϰ����/python��ϰ�ļ�/���Գ���.py", line 10, in <module>
# todo     a += i / b
# todo ZeroDivisionError: integer division or modulo by zero
# todo 这个错误是“ZeroDivisionError”，也就是除零错。
# todo “integer division or modulo by zero”，整数被0除或者被0模(取余数)。
# todo 因为0不能作为除数，所以当b随机到0的时候，就会引发这个错误。
# todo 知道了原因，就可以顺利地解决掉这个bug。
# todo 以后在写代码的时候，如果遇到了错误，先别急着去改代码。试着去读一读错误提示，看看里面都说了些啥。

# todo 2. 输出调试信息
# todo 我们在所有课程的最开始就教了输出函数“print”。它是编程中最简单的调试手段。有的时候，仅从错误提示仍然无法判断出程序错误的原因，或者没有发生错误，但程序的结果就是不对。这种情况下，通过输出程序过程中的一些状态，可以帮助分析程序。

# todo 把前面那个程序改造一下，加入一些与程序功能无关的输出语句：
import random
a = 0
for i in range(5):
    print 'i: %d' % i
    b = random.choice(range(5))
    print 'b: %d' % b
    a += i / b
    print 'a: %d' % a
    print
print a

# todo 运行后的输出结果（每次结果都会不一样）：
# todo i: 0
# todo b: 3
# todo a: 0
# todo i: 1
# todo b: 3
# todo a: 0
# todo i: 2
# todo b: 3
# todo a: 0
# todo i: 3
# todo b: 0
# todo Traceback (most recent call last):
# todo   File "C:\Users\Crossin\Desktop\py\test.py", line 7, in <module>
# todo     a += i / b
# todo ZeroDivisionError: integer division or modulo by zero
# todo 当b的值为0时，发生了除零错。这次可以更清晰地看出程序出错时的状态。
# todo 在真实开发中，程序的结构可能会非常复杂。通过输出调试信息，可以有效地缩小范围、定位错误发生的位置，确认错误发生时的场景，进而找出错误原因。