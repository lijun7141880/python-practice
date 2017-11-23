#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo 比如现在拿到一份文档，里面有某个班级里所有学生的平时作业成绩。因为每个人交作业的次数不一样，所以成绩的数目也不同，没交作业的时候就没有分。我现在需要统计每个学生的平时作业总得分。

# todo 看一下我们的文档里的数据：
# todo data/scores.txt
# todo 刘备 23 35 44 47 51
# todo 关羽 60 77 68
# todo 张飞 97 99 89 91
# todo 诸葛亮 100

# todo 1.先把文件读进来：
f = file('data/scores.txt')

# todo 2.取得文件中的数据。因为每一行都是一条学生成绩的记录，所以用readlines，把每一行分开，便于之后的数据处理：
lines = f.readlines()
print lines
f.close()

results = [] #results需要在循环之前初始化results = []

# todo 3.对每一条数据进行处理。按照空格，把姓名、每次的成绩分割开：
for line in lines:
   print line
   data = line.split()
   print data

# todo 4.整个程序最核心的部分到了。如何把一个学生的几次成绩合并，并保存起来呢？我的做法是：对于每一条数据，都新建一个字符串，把学生的名字和算好的总成绩保存进去。最后再把这些字符串一起保存到文件中：
   sum = 0 #每次循环中，sum都要先清零。
   for score in data[1:]: #对于每一行分割的数据，data[0]是姓名，data[1:]是所有成绩组成的列表。
       sum += int(score) #score是一个字符串，为了做计算，需要转成整数值int。
   result = '%s \t: %d\n' % (data[0], sum) #result中，加了一个制表符\t和换行符\n，让输出的结果更好看些
   print result

# todo 5.得到一个学生的总成绩后，把它添加到一个list中。
   results.append(result)

# todo 6.最后，全部成绩处理完毕后，把results中的内容保存至文件。因为results是一个字符串组成的list，这里我们直接用writelines方法：
print results
output = file('data/result.txt', 'w')
output.writelines(results)
output.close()