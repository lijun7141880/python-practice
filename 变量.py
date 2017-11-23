#!/usr/bin/python
# -*- coding: utf-8 -*-
# todo 变量，望文生义，就是变化的量。python里创建一个变量的方法很简单，给它起个名字，然后给它一个值。举起几个栗子:
# todo    name = 'Crossin'
# todo    myVar = 123
# todo    price = 5.99
# todo   visible = True
# todo“=”的作用是把右边的值赋予给左边的变量。
# todo 这里说一下另外一个概念，叫做“数据类型”，上面4颗栗子分别代表了python中较常见的四种基本类型：
# todo 字符串 - 表示一串字符，需要用''或""引起来
# todo 整数
# todo 浮点数 - 就是小数
# todo boolean（布尔） - 这个比较特殊，是用来表示逻辑“是”“非”的一种类型，它只有两个值，True和False。（注意这里没有引号，有了引号就变成字符串了，和javascript不同，要区分大小写）
# todo name = 'Crossin'
# todo print name

# todo 它叫变量，那就是能变的。所以在一次“赋值”操作之后，还可以继续给它赋予新的值，而且可以是不同类型的值。
# todo a = 123
# todo print a
# todo a = 'hi'
# todo print a

# todo“=”的右边还可以更复杂一点，比如是一个计算出的值:
# todo value = 3 * 4
# todo print value
# todo value = 2 < 5
# todo print value

# todo 甚至，也可以是input():

# todo name = input()
# todo print name

print "Who do you think I am?"
you = input()
print "Oh, yes! I am a"
print you