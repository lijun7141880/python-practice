#!/usr/bin/python
# -*- coding: utf-8 -*-
# todo list有两类常用操作：索引(index)和切片(slice)。
# todo 用[]加序号访问的方法就是索引操作。
# todo 除了指定位置进行索引外，list还可以处理负数的索引。
l = [365, 'everyday', 0.618, True]
print l[-1] #表示l中的最后一个元素。
print l[-3] #表示倒数第3个元素。

# todo 切片操作符是在[]内提供一对可选数字，用“:”分割。冒号前的数表示切片的开始位置，冒号后的数字表示切片到哪里结束。同样，计数从0开始。
# todo 注意，开始位置包含在切片中，而结束位置不包括。
print l[1:3]
# todo 得到的结果是['everyday', 0.618]。

# todo 如果不指定第一个数，切片就从列表第一个元素开始。
print l[:3]
# todo 如果不指定第二个数，就一直到最后一个元素结束。
print l[1:]
# todo 都不指定，则返回整个列表的一个拷贝。
print l[:]

# todo 同索引一样，切片中的数字也可以使用负数。比如：
print l[1:-1]
# todo 得到['everyday', 0.618]

# todo 点球小游戏升级版 5分死战局
from random import choice

score_you = 0
score_com = 0
direction = ['left', 'center', 'right']

for i in range(5):
   print '==== Round %d - You Kick! ====' % (i+1)
   print 'Choose one side to shoot:'
   print 'left, center, right'
   you = raw_input()
   print 'You kicked ' + you
   com = choice(direction)
   print 'Computer saved ' + com
   if you != com:
       print 'Goal!'
       score_you += 1
   else:
       print 'Oops...'
   print 'Score: %d(you) - %d(com)\n' % (score_you, score_com)

   print '==== Round %d - You Save! ====' % (i+1)
   print 'Choose one side to save:'
   print 'left, center, right'
   you = raw_input()
   print 'You saved ' + you
   com = choice(direction)
   print 'Computer kicked ' + com
   if you == com:
       print 'Saved!'
   else:
       print 'Oops...'
       score_com += 1
   print 'Score: %d(you) - %d(com)\n' % (score_you, score_com)
