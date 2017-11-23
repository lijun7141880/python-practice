#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo 如果我们要输出5个*，用for循环要这么写
for i in range(0, 5):
   print '*'
# todo 如果想让这5个*在同一行，python2的话就在print语句后面加上逗号
for i in range(0, 5):
   print '*',

# todo python3需要加上end参数：
# todo for i in range(0, 5):
# todo    print('*', end=' ')

# todo 但如果我想要这样一个图形，怎么办？
# todo * * * * *
# todo * * * * *
# todo * * * * *
# todo * * * * *
# todo * * * * *
for i in range(0, 5):
   print '* * * * *'

# todo 如果再进一步，这样呢？
# todo *
# todo **
# todo ***
# todo ****
# todo *****
print '*\n**\n***\n****\n*****'

# todo 除了你自己动手打好一个多行字符串外，也可以让程序帮我们解决这种问题，我们需要的是两个嵌套在一起的循环：
for i in range(0, 5):
   for j in range(0, 5):
       print i, j
# todo 第二个for循环在第一个for循环的内部，表示每一次外层的循环中，都要进行一遍内层的循环。
# todo 内层循环中的print语句一共被执行了25次。
# todo i从0到4循环了5次。对应于每一个i的值，j又做了从0到4五次循环。所以5*5一共25次。

# todo 所以如果要输出一个5*5的方阵图案，我们可以
for i in range(0, 5):
   for j in range(0, 5):
       print '*',
   print
# todo 第二个print的缩进和内层的for是一样的，这表明它是外层for循环中的语句，每次i的循环中，它会执行一次。
# todo print后面没有写任何东西，是起到换行的作用，这样，每输出5个 *，就会换行。

# todo 输出三角形*
for i in range(0, 5):
    for i in range(0, i+1):
        print '*',
    print