#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo python自带了功能丰富的标准库，另外还有数量庞大的各种第三方库。使用这些“巨人的”代码，可以让开发事半功倍，就像用积木一样拼出你要的程序。
# todo 使用这些功能的基本方法就是使用模块。通过函数，可以在程序里重用代码；通过模块，则可以重用别的程序中的代码。
# todo 模块可以理解为是一个包含了函数和变量的py文件。在你的程序中引入了某个模块，就可以使用其中的函数和变量。
# todo import语句告诉python，我们要用random模块中的内容。然后便可以使用random中的方法，比如：
import random
# todo 注意，函数前面需要加上“random.”，这样python才知道你是要调用random中的方法。
random.randint(1, 10)
random.choice([1, 3, 5])
# todo 想知道random有哪些函数和变量，可以用dir()方法：
print dir(random)

# todo 如果你只是用到random中的某一个函数或变量，也可以通过from...import...指明：
from math import pi
print pi

# todo 为了便于理解和避免冲突，你还可以给引入的方法换个名字：
from math import pi as math_pi
print math_pi