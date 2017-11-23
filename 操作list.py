#!/usr/bin/python
# -*- coding: utf-8 -*-
# todo 假设我们现在有一个list：
l = [365, 'everyday', 0.618, True]
# todo 除了用for...in遍历l中的元素，我们还能做点啥？

# todo 1. 访问list中的元素
# todo list中的每个元素都对应一个递增的序号。与现实中习惯的序号不同在于，计算机中的计数通常都是从0开始，python也不例外。\
# todo 要访问l中的第1个元素365，只要用l[0]就可以了。依次类推，
print l[1]
# todo 就会输出'everyday'
# todo 注意，你不能访问一个不存在的元素，比如l[10]，程序就会报错，提示你index越界了。

# todo 2. 修改list中的元素
# todo 修改list中的某一个元素，只需要直接给那个元素赋值就可以了：
l[0] = 123
print l
# todo 输出l，得到[123, 'everyday', 0.618, True]，第1个元素已经从365被改成了123。

# todo 3. 向list中添加元素
# todo list有一个append方法，可以增加元素。以l这个列表为例，调用的方法是：
l.append(1024)
print l
# todo 输出l，你会看到[123, 'everyday', 0.618, True, 1024]，1024被添加到了l，成为最后一个元素。（第一个元素在上一步被改成了123）
# todo 然后同样可以用l[4]得到1024。

# todo 4. 删除list中的元素
# todo 删除list中的某一个元素，要用到del：
del l[0]
print l
# todo 输出l，得到['everyday', 0.618, True, 1024]。这时候再调用l[0]，会得到'everyday'，其他元素的序号也相应提前。

# todo 点球小游戏

from random import choice
print 'Choose one side to shoot:'
print 'left, center, right'
you = raw_input()
print 'You kicked ' + you
direction = ['left', 'center', 'right']
com = choice(direction)
print 'Computer saved ' + com
if you != com:
   print 'Goal!'
else:
   print 'Oops...'