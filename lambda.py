#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo lambda 表达可以被看做是一种匿名函数。它可以让你快速定义一个极度简单的单行函数。
# todo 譬如这样一个实现三个数相加的函数：
def sum(a, b, c):
    return a + b + c


print sum(1, 2, 3)  # 6
print sum(4, 5, 6)  # 15

# todo 如果使用 lambda 表达式来实现：

sum = lambda a, b, c: a + b + c

print sum(1, 2, 3)  # 6
print sum(4, 5, 6)  # 15


# todo lambda 表达式的语法格式：lambda 参数列表: 表达式
# todo 定义 lambda 表达式时，参数列表周围没有括号，返回值前没有 return 关键字，也没有函数名称。
# todo 它的写法比 def 更加简洁。但是，它的主体只能是一个表达式，不可以是代码块，甚至不能是命令（print 不能用在 lambda 表达式中）。所以 lambda 表达式能表达的逻辑很有限。
# todo lambda 表达式创建了一个函数对象，可以把这个对象赋值给一个变量进行调用，就像上面的例子中一样。

# todo 把 lambda 表达式用在 def 函数定义中：
def fn(x):
    return lambda y: x + y


a = fn(2)
print a(3)  # 5
# todo 这里，fn 函数的返回值是一个 lambda 表达式，也就等于是一个函数对象。当以参数2来调用 fn 时，得到的结果就是：lambda y: 2 + y
# todo a = fn(2) 就相当于：a = lambda y: 2 + y
# todo 所以 a(3) 的结果就是5。

# todo lambda 表达式其实只是一种编码风格，这种写法更加 pythonic。这并不意味着你一定要使用它。事实上，任何可以使用 lambda 表达式的地方，都可以通过普通的 def 函数定义来替代。在一些需要重复使用同一函数的地方，def 可以避免重复定义函数。况且 def 函数更加通用，某些情况可以带来更好地代码可读性。

# todo 而对于像 filter、sort 这种需要内嵌函数的方法，lambda 表达式就会显得比较合适。
