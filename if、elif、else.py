#!/usr/bin/python
# -*- coding: utf-8 -*-
# todo if是：“如果”条件满足，就做xxx，否则就不做。
# todo else顾名思义，就是：“否则”就做yyy。
# todo 当if后面的条件语句不满足时，与之相对应的else中的代码块将被执行。
a = input()
if a == 1:
   print 'right'
else:
   print 'wrong'

# todo elif意为else if，含义就是：“否则如果”条件满足，就做yyy。elif后面需要有一个逻辑判断语句。
# todo 当if条件不满足时，再去判断elif的条件，如果满足则执行其中的代码块。
a = input()
if a == 1:
   print 'one'
elif a == 2:
   print 'two'

# todo if, elif, else可组成一个整体的条件语句。
a = input()
if a == 1:
   print 'one'
elif a == 2:
   print 'two'
elif a == 3:
   print 'three'
else:
   print 'too many'

# todo if, elif, else改写小游戏中的函数isEqual。
def isEqual(num1, num2):
   if num1<num2:
       print 'too small'
       return False
   elif num1>num2:
       print 'too big'
       return False
   else:
       print 'bingo'
       return True

from random import randint
sum = randint(1, 1000)
flag = False
while flag == False:
    answer = int(input())
    isEqual(answer, sum)