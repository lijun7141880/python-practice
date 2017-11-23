#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo random模块的作用是产生随机数。
# todo random.randint(a, b)可以生成一个a到b间的随机整数，包括a和b。
# todo a、b都必须是整数，且必须b≥a。当等于的时候，比如：
# todo random.randint(3, 3)
# todo 的结果就永远是3

# todo random.random()  生成一个0到1之间的随机浮点数，包括0但不包括1，也就是[0.0, 1.0)。

# todo random.uniform(a, b)  生成a、b之间的随机浮点数。不过与randint不同的是，a、b无需是整数，也不用考虑大小。
# todo random.uniform(1.5, 3)
# todo random.uniform(3, 1.5)
# todo 这两种参数都是可行的。
# todo random.uniform(1.5, 1.5)永远得到1.5。

# todo random.choice(seq)  从序列中随机选取一个元素。seq需要是一个序列，比如list、元组、字符串。
# todo 从序列中随机选取一个元素。seq需要是一个序列，比如list、元组、字符串。
# todo random.choice([1, 2, 3, 5, 8, 13]) #list
# todo random.choice('hello') #字符串
# todo random.choice(['hello', 'world']) #字符串组成的list
# todo random.choice((1, 2, 3)) #元组
# todo 都是可行的用法。

# todo random.randrange(start, stop, step)  生成一个从start到stop（不包括stop），间隔为step的一个随机数。start、stop、step都要为整数，且start<stop。
# todo random.randrange(1, 9, 2)
# todo 就是从[1, 3, 5, 7]中随机选取一个。
# todo start和step都可以不提供参数，默认是从0开始，间隔为1。但如果需要指定step，则必须指定start。
# todo random.randrange(4) #[0, 1, 2, 3]
# todo random.randrange(1, 4) #[1, 2, 3]
# todo random.randrange(start, stop, step)其实在效果上等同于  random.choice(range(start, stop, step))

# todo random.sample(population, k)  从population序列中，随机获取k个元素，生成一个新序列。sample不改变原来序列。

# todo random.shuffle(x)  把序列x中的元素顺序打乱。shuffle直接改变原有的序列。