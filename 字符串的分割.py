#!/usr/bin/python
# -*- coding: utf-8 -*-
# todo 字符串和list之间有很多关联，比如想要用python去自动抓取某个网页上的下载链接，那就需要对网页的代码进行处理。处理的过程中，免不了要在字符串和list之间进行很多操作。
# todo 假设现在拿到了一个英语句子，需要把这个句子中的每一个单词拿出来单独处理。
sentence = 'I am an Englist sentence'
# todo 这时就需要对字符串进行分割。
print sentence.split()
# todo split()会把字符串按照其中的空格进行分割，分割后的每一段都是一个新的字符串，最终返回这些字符串组成一个list。于是得到
# todo ['I', 'am', 'an', 'Englist', 'sentence']
# todo 除了空格外，split()同时也会按照换行符\n，制表符\t进行分割。所以应该说，split默认是按照空白字符进行分割。

# todo 之所以说默认，是因为split还可以指定分割的符号。比如你有一个很长的字符串
section = 'Hi. I am the one. Bye.'
# todo 通过指定分割符号为'.'，可以把每句话分开
print section.split('.')
# todo 得到['Hi', ' I am the one', ' Bye', '']
# todo 这时候，'.'作为分割符被去掉了，而空格仍然保留在它的位置上。
# todo 注意最后那个空字符串。每个'.'都会被作为分割符，即使它的后面没有其他字符，也会有一个空串被分割出来。例如
print 'aaa'.split('a')
# todo 将会得到['', '', '', '']，由四个空串组成的list。

# todo 点球大战小游戏升级版 如果5轮结束之后是平分，就继续踢。
from random import choice

score = [0, 0]
direction = ['left', 'center', 'right']

def kick():
   print '==== You Kick! ===='
   print 'Choose one side to shoot:'
   print 'left, center, right'
   you = raw_input()
   print 'You kicked ' + you
   com = choice(direction)
   print 'Computer saved ' + com
   if you != com:
       print 'Goal!'
       score[0] += 1
   else:
       print 'Oops...'
   print 'Score: %d(you) - %d(com)\n' % (score[0], score[1])

   print '==== You Save! ===='
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
       score[1] += 1
   print 'Score: %d(you) - %d(com)\n' % (score[0], score[1])

for i in range(5):
   print '==== Round %d ====' % (i+1)
   kick()

while(score[0] == score[1]):
   i += 1
   print '==== Round %d ====' % (i+1)
   kick()

if score[0] > score[1]:
   print 'You Win!'
else:
   print 'You Lose.'