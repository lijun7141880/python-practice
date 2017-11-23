#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo while循环在条件不满足时结束，for循环遍历完序列后结束。如果在循环条件仍然满足或序列没有遍历完的时候，想要强行跳出循环，就需要用到break语句。
while True:
   a = raw_input()
   if a == 'EOF':
       break
# todo 上面的程序不停接受用户输入。当用户输入一行“EOF”时，程序结束。

for i in range(10):
   a = raw_input()
   if a == 'EOF':
       break

# todo 上面的程序接受用户10次输入，当用户输入一行“EOF”时，程序提前结束。

# todo 猜数字小游戏如果猜负数则结束游戏
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

from random import randint
sum = randint(1, 1000)
flag = False
while flag == False:
    answer = int(input())
    isEqual(answer, sum)
    if answer < 0:
        print 'exit game !'
        break