#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo 同while一样，for循环可以用来重复做一件事情。在某些场景下，它比while更好用。
# todo for循环的本质是对一个序列中的元素进行递归。
# todo for i in range(a, b)  从a循环至b-1

# todo 习题 输出1到100
# todo for i in range(1, 101):
# todo     print i

# todo for循环，从1加到100等于多少？
# todo sum = 0
# todo for i in range(1, 101):
# todo     sum += i
# todo     print sum

# todo 输入一个值，输出以这个值为公比，1为首项的等比数列前10项
# todo while循环
# todo num = int(input())
# todo a = 1
# todo an = 1
# todo while a <= 10:
# todo     print an
# todo     an *= num
# todo    a += 1

# todo for循环
# todo num = int(input())
# todo a = 1
# todo for i in range(0, 10):
# todo     print a
# todo     a *= num

# todo 输入一个大于等于3的值n，输出斐波那契数列的前n项。
# todo 注：斐波那契数列：1,1,2,3,5,8,13,21...前两项为1，从第三项起，每一项是前两项的和
# todo while循环
# todo num = int(input())
# todo x = 3
# todo a1 = 1
# todo a2 = 1
# todo print a1
# todo print a2
# todo while x <= num:
# todo    a3 = a1 + a2
# todo    a1 = a2
# todo    a2 = a3
# todo     print a3
# todo    x += 1

# todo for循环
num = int(input())
a1 = 1
a2 = 1
print a1
print a2
for i in range(3, num+1):
    a3 = a1 + a2
    a1 = a2
    a2 = a3
    print a3
