#!/usr/bin/python
# -*- coding: utf-8 -*-
# todo 程序执行到while处，“当”条件为True时，就去执行while内部的代码，“当”条件为False时，就跳过。
# todo 语法为：
# todo    while 条件:
# todo        循环执行的语句
# todo 同if一样，注意冒号，注意缩进

# todo 猜谜小游戏
num = 10
bigon = False
while bigon == False:
    answer = input()
    if answer < num:
        print ("too small !")
    if answer > num:
        print ("too big !")
    if answer == num:
        print ("bigon !")
        bigon = True
