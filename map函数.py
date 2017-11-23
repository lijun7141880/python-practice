#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo 1. 假设有一个数列，如何把其中每一个元素都翻倍？

lst_1 = [1, 2, 3, 4, 5, 6]
lst_2 = []
for i in lst_1:
    lst_2.append(i * 2)
print lst_2  # [2, 4, 6, 8, 10, 12]

# todo 或者：
lst_1 = [1, 2, 3, 4, 5, 6]
lst_2 = [i * 2 for i in lst_1]
print lst_2  # [2, 4, 6, 8, 10, 12]

# todo 另一种写法 map:
st_1 = [1, 2, 3, 4, 5, 6]


def double_func(x):
    return x * 2


lst_2 = map(double_func, lst_1)
print lst_2  # [2, 4, 6, 8, 10, 12]
# todo map 是 Python 自带的内置函数，它的作用是把一个函数应用在一个（或多个）序列上，把列表中的每一项作为函数输入进行计算，再把计算的结果以列表的形式返回。
# todo map 的第一个参数是一个函数，之后的参数是序列，可以是 list、tuple。

# todo 或者：
lst_1 = (1, 2, 3, 4, 5, 6)
lst_2 = map(lambda x: x * 2, lst_1)  # lambda x: x * 2 是一个函数，作为第一个参数， lst_1作为第二个参数
print lst_2  # [2, 4, 6, 8, 10, 12]

# todo 2. 假设有两个数列，如何求和？

lst_1 = [1, 2, 3, 4, 5, 6]
lst_2 = [1, 3, 5, 7, 9, 11]
lst_3 = map(lambda x, y: x + y, lst_1, lst_2)
print lst_3  # [2, 5, 8, 11, 14, 17]

# todo map 中的函数会从对应的列表中依次取出元素，作为参数使用，同样将结果以列表的形式返回。所以要注意的是，函数的参数个数要与 map 中提供的序列组数相同，即函数有几个参数，就得有几组数据。

# todo 对于每组数据中的元素个数，如果有某组数据少于其他组，map 会以 None 来补全这组参数。

# todo 此外，当 map 中的函数为 None 时，结果将会直接返回参数组成的列表。如果只有一组序列，会返回元素相同的列表，如果有多组数列，将会返回每组数列中，对应元素构成的元组所组成的列表。

lst_1 = [1, 2, 3, 4, 5, 6]
lst_2 = [1, 3, 5, 7, 9, 11]
lst_3 = map(None, lst_1)
print lst_3  # [1, 2, 3, 4, 5, 6] map中函数为None，并且只有一组序列，所以返回相同的列表
lst_4 = map(None, lst_1, lst_2)
print lst_4  # [(1, 1), (2, 3), (3, 5), (4, 7), (5, 9), (6, 11)] map中函数为None，并且有多组序列，返回的是对应元素构成的元组所组成的列表。
