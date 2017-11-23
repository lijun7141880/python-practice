#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo 所谓列表解析（也有翻译成列表综合），就是通过一个已有的列表生成一个新的列表。
# todo 假设有一个由数字组成的 list，现在需要把其中的偶数项取出来，组成一个新的 list。
# todo 第一种方法是：
list_1 = [1, 2, 3, 5, 8, 13, 22]
list_2 = []
for i in list_1:
    if i % 2 == 0:
        list_2.append(i)
print list_2  # [2, 8, 22]

# todo 第二种方法是：使用列表解析
list_1 = [1, 2, 3, 5, 8, 13, 22]
list_2 = [i for i in list_1 if i % 2 == 0]
print list_2  # [2, 8, 22]
# todo [i for i in list_1] 会把 list_1 中的每一个元素都取出来，构成一个新的列表。
# todo 如果需要对其中的元素进行筛选，就在后面加上判断条件 if。所以 [i for i in list_1 if i % 2 == 0] 就是把 list_1 中满足 i % 2 == 0 的元素取出来组成新列表。
# todo 进一步的，在构建新列表时，还可以对于取出的元素做操作。比如，对于原列表中的偶数项，取出后要除以2，则可以通过 [i / 2 for i in list_1 if i % 2 == 0] 来实现。输出为 [1, 4, 11]。
# todo 在实际开发中，适当地使用列表解析可以让代码更加简洁、易读，降低出错的可能。

# todo 习题：
# todo 用一行 Python 代码实现：把1到100的整数里，能被2、3、5整除的数取出，以分号（;）分隔的形式输出。
print ';'.join([str(i) for i in range(1, 101) if i % 2 == 0 or i % 3 == 0 or i % 5 == 0])