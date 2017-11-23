#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo map 可以看作是把一个序列根据某种规则，映射到另一个序列。reduce 做的事情就是把一个序列根据某种规则，归纳为一个输出。
# todo 求1累加到100的和。
# todo 普通方法
sum = 0
for i in range(1, 101):
    sum += i
print sum

# todo reduce方法
lst = xrange(1, 101)


def add(x, y):
    return x + y


print reduce(add, lst)

# todo reduce(function, iterable[, initializer])
# todo 第一个参数是作用在序列上的方法，第二个参数是被作用的序列，这与 map 一致。另外有一个可选参数，是初始值。
# todo function 需要是一个接收2个参数，并有返回值的函数。它会从序列 iterable 里从左到右依次取出元素，进行计算。每次计算的结果，会作为下次计算的第一个参数。
# todo 提供初始值 initializer 时，它会作为第一次计算的第一个参数。否则，就先计算序列中的前两个值。


# todo 同样，可以用 lambda 函数：
print reduce((lambda x, y: x + y), xrange(1, 101))

# todo Python3 里，reduce已经被移出内置函数，使用 reduce 需要先通过 from functools import reduce 引入。