#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo 在最早我们开发的那个猜数字游戏的基础上，增加保存成绩的功能。
# todo 我现在打算记录下我玩了多少次，最快猜出来的轮数，以及平均每次猜对用的轮数。
# todo 于是，我要在文件中记录3个数字，如：
# todo 3 5 31
# todo 它们分别是：总游戏次数，最快猜出的轮数，和猜过的总轮数（这里我选择记录总轮数，然后每次再算出平均轮数）

# todo 1.首先,新建好一个game.txt，里面写上：
# todo 0 0 0
# todo 作为程序的初始数据。

# todo 2.读取数据
f = open('data/game.txt')
score = f.read().split()

# todo 3.为便于理解，把数据读进来后，分别存在3个变量中。
game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])

# todo 4.平均轮数根据总轮数和游戏次数相除得到：
# todo 注意两点：
# todo 1.我在total_times前加上了float，把它转成了浮点数类型再进行除法运算。如果不这样做，两个整数相除的结果会默认为整数，而且不是四舍五入。
# todo 2.因为0是不能作为除数的，所以这里还需要加上判断：
if game_times > 0:
    avg_times = float(total_times) / game_times
else:
    avg_times = 0

# todo 5.然后，在让玩家开始猜数字前，输出他之前的成绩信息：
print '你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案' % (game_times, min_times, avg_times)

# todo 6.我们需要有一个变量来记录每次游戏所用的轮数：
times = 0

# todo 7.然后在游戏每进行一轮的时候，累加这个变量：
times += 1

# todo 8.如果是第一次玩，或者本次的轮数比最小轮数还少，就记录本次成绩为最小轮数：
if game_times == 0 or times < min_times:
    min_times = times

# todo 9.把本次轮数加到游戏总轮数里：
total_times += times

# todo 10.把游戏次数加1：
game_times += 1

# todo 11.现在有了我们需要的数据，把它们拼成我们需要存储的格式：
result = '%d %d %d'%(game_times,min_times,avg_times)

# todo 12.写入到文件中：
f = open('data/game.txt', 'w')
f.write(result)
f.close()

# todo 小游戏现在已经可以保存成绩了，但只有一组成绩，不管谁来玩，都会算在里面。所以还要加上一个更多的功能：存储多组成绩。玩家需要做的就是，在游戏开始前，输入自己的名字。而我会根据这个名字记录他的成绩。这个功能所用到的内容我们几乎都说过，现在要把它们结合起来。
# todo 12.首先要输入名字，这是我们用来区分玩家成绩的依据：
name = raw_input('请输入你的名字：')

# todo 13.接下来，我们读取文件。与之前不同，我们用readlines把每组成绩分开来：
f = open('data/game.txt')
lines = f.readlines()

# todo 14.再用一个字典来记录所有的成绩：
scores = {}
for l in lines:
   s = l.split()
   scores[s[0]] = s[1:]

# todo 15.我们要找到当前玩家的数据：
score = scores.get(name)

# todo 16.所以如果没有找到该玩家的数据，说明他是一个新玩家，我们给他初始化一组成绩：
if score is None:
   score = [0, 0, 0]

# todo 我们不能直接把这次成绩存到文件里，那样就会覆盖掉别人的成绩。必须先把成绩更新到scores字典中，再统一写回文件中。

# todo 17.把成绩更新到scores中，如果没有这一项，会自动生成新条目：
scores[name] = [str(game_times), str(min_times), str(total_times)]

# todo 18.对于每一项成绩，我们要将其格式化：
result = ''
for n in scores:
   line = n + ' ' + ' '.join(scores[n]) + '\n'
   result += line

# todo 19.把scores中的每一项按照“名字 游戏次数 最低轮数 总轮数\n”的格式拼成字符串，再全部放到result里，就得到了我们要保存的结果。
result = '%d %d %d' % (game_times, min_times, avg_times)

# todo 20.最后就和之前一样，把result保存到文件中。
f = open('data/game.txt', 'w')
f.write(result)
f.close()