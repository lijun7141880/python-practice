#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo break是彻底地跳出循环，而continue只是略过本次循环的余下内容，直接进入下一次循环。
# todo 无论是continue还是break，其改变的仅仅是当前所处的最内层循环的运行，如果外层还有循环，并不会因此略过或跳出。

# todo 在脑中模拟运行下面这段程序，想想会输出什么结果。再敲到代码里验证一下：
i = 0
while i < 5:
   i += 1
   for j in range(3):
       print j
       if j == 2:
           break
   for k in range(3):
       if k == 2:
           continue
       print k
   if i > 3:
       break
   print i
# todo 预测结果 0 1 2 0 1 1 0 1 2 0 1 2 0 1 2 0 1 3 0 1 2 0 1