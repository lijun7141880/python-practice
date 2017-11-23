#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo Python中有一个time模块，它提供了一些与时间相关的方法。利用time，可以简单地计算出程序运行的时间。对于一些比较复杂、耗时较多的程序，可以通过这种方法了解程序中哪里是效率的瓶颈，从而有针对性地进行优化。
# todo 在计算机领域有一个特殊的时间，叫做epoch，它表示的时间是1970-01-01 00:00:00 UTC。
# todo Python中time模块的一个方法
# todo time.time()
# todo 返回的就是从epoch到当前的秒数（不考虑闰秒）。这个值被称为unix时间戳。

import time
starttime = time.time()
print 'start:%f' % starttime
for i in range(10):
    print i
endtime = time.time()
print 'end:%f' % endtime
print 'total time:%f' % (endtime-starttime)

# todo 在程序中的不同位置调用time.time()就可以得到运行到那个地方的时间，了解不同部分消耗的时间。

# todo time.sleep(secs)  它可以让程序暂停secs秒
import time
print 1
time.sleep(3)
print 2

# todo 在抓取网页的时候，适当让程序sleep一下，可以减少短时间内的请求，提高请求的成功率。