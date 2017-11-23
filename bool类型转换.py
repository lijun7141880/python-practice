#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo 在python中，以下数值会被认为是False：
# todo 为0的数字，包括0，0.0
# todo 空字符串，包括''，""
# todo 表示空值的None
# todo 空集合，包括()，[]，{}
# todo 其他的值都认为是True。
# todo None是python中的一个特殊值，表示什么都没有，它和0、空字符、False、空集合都不一样。
# todo 在if、while等条件判断语句里，判断条件会自动进行一次bool的转换。
# todo比如
# todo   a = '123'
# todo  if a:
# todo      print 'this is not a blank string'
# todo 这在编程中是很常见的一种写法。效果等同于
# todo if bool(a)
# todo 或者
# todo if a != ''
