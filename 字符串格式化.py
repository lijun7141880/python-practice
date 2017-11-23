#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo 我们在输出字符串的时候，如果想对输出的内容进行一些整理，比如把几段字符拼接起来，或者把一段字符插入到另一段字符中间，就需要用到字符串的格式化输出。

# todo 如果你想把两段字符连起来输出
# todo str1 = 'good'
# todo str2 = 'bye'

# todo 你可以
# todo print str1 + str2

# todo 或者还可以把字符变量一个字符串相加
# todo print 'very' + str1
# todo print str1 + ' and ' + str2

# todo 但如果你想要把一个数字加到文字后面输出，比如这样
# todo num = 18
# todo print 'My age is' + num
# todo 程序就会报错。因为字符和数字不能直接用+相加。

# todo 一种解决方法是，用str()把数字转换成字符串
# todo print 'My age is' + str(18)
# todo 或
# todo num = 18
# todo print 'My age is' + str(num)

# todo 还有一种方法，就是用%对字符串进行格式化
# todo num = 18
# todo print 'My age is %d' % num
# todo 输出的时候，%d会被%后面的值替换。输出
# todo My age is 18

# todo 这里，%d只能用来替换整数。如果你想格式化的数值是小数，要用%f
# todo print ‘Price is %f’ % 4.99
# todo 输出
# todo Price is 4.990000

# todo 如果你想保留两位小数，需要在f前面加上条件：%.2f
# todo print ‘Price is %.2f’ % 4.99
# todo 输出
# todo Price is 4.99

# todo 另外，可以用%s来替换一段字符串
# todo name = 'Crossin'
# todo print '%s is a good teacher.' % name
# todo 输出
# todo Crossin is a good teacher.

# todo 注意区分：有引号的表示一段字符，没有引号的就是一个变量，这个变量可能是字符，也可能是数字，但一定要和%所表示的格式相一致。

# todo 改写小游戏
from random import randint
num = randint(1, 1000)
flag = False
while flag == False:
    a = int(input())
    if a < num:
        print str(a) + ' too small !'
    if a > num:
        print str(a) + ' too big !'
    if a == num:
        print str(num) + ' bingo !'
        flag = True
