#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo 引入模块的方法：
# todo    from 模块名 import 方法名
# todo 注意文件名与要引入的模块名不能相同
from random import randint

num = randint(1, 1000)
bingo = False
while bingo == False:
    answer = input()
    if answer < num:
        print ("too small !")
    if answer > num:
        print ("too big !")
    if answer == num:
        print ("bigon !")
        bingo = True
