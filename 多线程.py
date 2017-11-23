#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo 很多人使用 python 编写“爬虫”程序，抓取网上的数据。

# todo 举个例子，通过豆瓣的 API 抓取 30 部影片的信息：
import urllib, time

time_start = time.time()
data = []
for i in range(30):
    print 'request movie:', i
    id = 1764796 + i
    url = 'https://api.douban.com/v2/movie/subject/%d' % id
    d = urllib.urlopen(url).read()
    data.append(d)
    print i, time.time() - time_start

print 'data:', len(data)

# todo 参考输出结果：
# request movie: 0
# 0 0.741228103638
# request movie: 1
# 1 1.96586918831
# ...
# request movie: 28
# 28 12.0225770473
# request movie: 29
# 29 12.4063940048
# data: 30

# todo 程序里用了 time.time() 来计算抓取花费的时间。运行一遍，大约需要十几秒（根据网络情况会有差异）。
# todo 如果我们想用这套代码抓取几万部电影，就算中间不出什么状况，估计也得花上好几个小时。

# todo 我们抓一部电影信息的过程是独立，并不依赖于其他电影的结果。因此没必要排好队一部一部地按顺序来。
# todo 可以使用多线程同时抓取好几部电影。

# todo python 里有一个 thread 模块，其中提供了一个函数：start_new_thread(function, args[, kwargs])
# todo function 是开发者定义的线程函数，
# todo args 是传递给线程函数的参数，必须是tuple类型，
# todo kwargs 是可选参数。

# todo 调用 start_new_thread 之后，会创建一个新的线程，来执行 function 函数。而代码原本的主线程将继续往下执行，不再等待 function 的返回。通常情况，线程在 function 执行完毕后结束。

# todo 改写一下前面的代码，将抓取的部分放在一个函数中：

import urllib, time, thread

def get_content(i):
    id = 1764796 + i
    url = 'https://api.douban.com/v2/movie/subject/%d' % id
    d = urllib.urlopen(url).read()
    data.append(d)
    print i, time.time() - time_start
    print 'data:', len(data)

time_start = time.time()
data = []
for i in range(30):
    print 'request movie:', i
    thread.start_new_thread(get_content, (i,))

raw_input('press ENTER to exit...\n')


# todo 参考输出结果：
# request movie: 0
# request movie: 1
# ...
# request movie: 28
# request movie: 29
# press ENTER to exit...
# 1 0.39500784874
# data: 1
# 9 0.428859949112
# data: 2
# ...
# data: 28
# 21 1.03756284714
# data: 29
# 8 2.66121602058
# data: 30

# todo 因为主线程不在等待函数返回结果，所以在代码最后，增加了 raw_input，避免程序提前退出。

# todo 从输出结果可以看出：
# todo 1.在程序刚开始运行时，已经发送所有请求
# todo 2.收到的请求并不是按发送顺序，先收到就先显示
# todo 3.总共用时两秒多
# todo 4.data 里同样记录了所有30条结果

# todo 所以，对于这种耗时长，但又独立的任务，使用多线程可以大大提高运行效率。但在代码层面，可能额外需要做一些处理，保证结果正确。如上例中，如果需要电影信息按 id 排列，就要另行排序。
# todo 多线程通常会用在网络收发数据、文件读写、用户交互等待之类的操作上，以避免程序阻塞，提升用户体验或提高执行效率。
# todo 多线程的实现方法不止这一种。另外多线程也会带来一些单线程程序中不会出现的问题。