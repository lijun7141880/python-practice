#!/usr/bin/python
# -*- coding: utf-8 -*-
# todo 我希望有这样一个函数，它比较两个数的大小。
# todo 如果第一个数小了，就输出“too small”
# todo 如果第一个数大了，就输出“too big”
# todo 如果相等，就输出“bingo”
# todo 函数还有个返回值，当两数相等的时候返回True，不等就返回False。

def isEqual(num1, num2):
    if num1 < num2:
        print 'too small !'
        return False
    if num1 > num2:
        print 'too big !'
        return False
    if num1 == num2:
        print 'bingo!'
        return True
isEqual(5, 5)

# todo 这里说一下，return是函数的结束语句，return后面的值被作为这个函数的返回值。函数中任何地方的return被执行到的时候，这个函数就会结束。

# todo 在猜数字小游戏里使用这个函数
# todo 在isEqual函数内部，会输出answer和sum的比较结果，如果相等的话，flag会得到返回值True，否则flag得到False，循环继续。
from random import randint
sum = randint(1, 1000)
flag = False
while flag == False:
    answer = int(input())
    flag = isEqual(answer, sum)

# todo 函数可以把某个功能的代码分离出来，在需要的时候重复使用，就像拼装积木一样，这会让程序结构更清晰。
