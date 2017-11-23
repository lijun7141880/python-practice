#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo 逻辑判断在编程中是非常重要的。大量的复杂程序在根本上都是建立在“真”与“假”的基本逻辑之上。而bool所表示的就是这种最单纯最本质的True/False，真与假，是与非
# todo thisIsLove = input()
# todo if    thisIsLove:
# todo        print "再转身就该勇敢留下来"

num = 10
print 'Guess what I think?'
answer = int(input())
if answer < num:
    print 'too small!'
if answer > num:
    print 'too big!'
if answer == num:
    print 'BINGO!'
