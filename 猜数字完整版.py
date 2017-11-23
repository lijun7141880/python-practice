#!/usr/bin/python
# -*- coding: utf-8 -*-
# from random import randint #导入随机数模块
#
# name = raw_input('输入你的名字：') #name变量保存输入的名字
#
# f = open('data/game.txt') #打开data目录下的game.txt文件
# lines = f.readlines() #把内容按行读取至一个list中 ['hanhonglei 4 7 37\n']
# f.close() #关闭文件
#
# scores = {} #定义一个字典
# for l in lines: #对list进行遍历，i为list中的每一项 hanhonglei 4 7 37
#     s = l.split() #对list中的项进行分割，'hanhonglei', '4', '7', '37'
#     scores[s[0]] = s[1:] #s[0]代表的是name，所以这句话的意思是scores[name] = s[1:]，也就是['4','7','13']
# score = scores.get(name) #对name进行查找
# if score is None: #如果没有name
#     score = [0, 0, 0] #就初始化一个新的name，并赋予[0,0,0]
#
# game_times = int(score[0]) #游戏次数为score中第一个数字
# min_times = int(score[1]) #猜数字最小次数为score中第二个数字
# total_times = int(score[2]) #总共猜了多少次为score中第三个数字
#
# if game_times > 0: #如果游戏次数大于0
#     avg_times = float(total_times) / game_times #平均猜对率为总次数处于游戏次数，由于整数与整数相除默认四舍五入，所以我们要加float
# else: #否则
#     avg_times = 0 #平均猜对率为0
#
# print '%s, 您已经玩了%d次游戏，最快猜对次数为%d，平均猜对次数为%d'%(name,game_times,min_times,avg_times) #输入名字后显示上次游戏信息
#
# num = randint(1, 1000) #定义一个随机数
# times = 0 #每轮猜数字的轮数
# bingo = False #假设一个变量为False
# while bingo == False: #当bingo为False时
#     answer = int(input('请输入数字：')) #定义一个变量为我们输入的数字，最好转化为int类型
#     times += 1 #输入一次轮数加一次
#     if answer < num: #当输入的数字小于系统给的随机数时
#         print ("%d too small !")%(answer) #输出数字太小，用字符串格式化替换数字
#         bingo = False #bingo为False，继续循环
#     if answer > num: #当输入的数字大于系统给的随机数时
#         print ("%d too big !")%(answer) #输出数字太大，用字符串格式化替换数字
#         bingo = False #bingo为False，继续循环
#     if answer == num: #当输入的数字和系统给的随机数相等时
#         print ("%d bigon !")%(answer) #输出bingo
#         bingo = True #bingo为True，停止循环
#
# if game_times == 0 or times < min_times: #如果是第一次玩游戏或者猜对次数小于最小次数
#     min_times = times #用当前猜对的次数替换最小的次数
# total_times += times #总次数为上次的总次数加上当前的次数
# game_times += 1 #游戏次数加1
#
# scores[name] = [str(game_times), str(min_times), str(total_times)] #将得到的新次数更新到scores中
# result = '' #定义一个空字符串
# for i in scores: #遍历scores i为scores[name]
#     line = i + ' ' + ' '.join(scores[i]) + '\n' #把 hanhonglei拼接一个空格，把['4','7','13']格式的list通过空格，连接成[4 7 13]的格式，在末尾加换行符。最后的格式为 hanhonglei 4 7 13
#     result += line #把得到的新的行加入到result中
#
# f = open('data/game.txt', 'w') #打开data目录下的game.txt文件
# f.write(result) #把result写入到文件中替换掉旧的内容
# f.close() #关闭文件

from random import randint

name = raw_input('请输入您的名字：')
f = open('data/game.txt')
lines = f.readlines()
f.close()
scores = {}
for l in lines:
    s = l.split()
    scores[s[0]] = s[1:]
score = scores.get(name)
if score is None:
    score = [0, 0, 0]
game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])
if game_times > 0:
    avg_times = float(total_times) / game_times
else:
    avg_times = 0
print '%s,这是您的第%d次游戏，您的最好成绩为%d，您的平均成绩为%.2f'%(name,game_times,min_times,avg_times)
num = randint(1, 1000)
times = 0
bingo = False
while bingo == False:
    answer = int(input('请输入数字：'))
    times += 1
    if answer < num:
        print '%d is too small !'%(answer)
        bingo = False
    if answer > num:
        print '%d is too big !'%(answer)
        ningo = False
    if answer == num:
        print '%d is bingo !'%(answer)
        bingo = True
if game_times == 0 or times < min_times:
    min_times = times
game_times += 1
total_times += times
scores[name] = [str(game_times), str(min_times), str(total_times)]
result = ''
for i in scores:
    line = i + ' ' + ' '.join(scores[i]) + '\n'
    result += line
f = open('data/game.txt', 'w')
f.write(result)
f.close()