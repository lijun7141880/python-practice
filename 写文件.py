#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo 写文件也需要三步：
# todo 打开文件；
# todo 把内容写入文件；
# todo 关闭文件。

# todo python默认是以只读模式打开文件。如果想要写入内容，在打开文件的时候需要指定打开模式为写入：
# todo 'w'就是writing，以这种模式打开文件，原来文件中的内容会被你新写入的内容覆盖掉，如果文件不存在，会自动创建文件。
# todo 不加参数时，file为你默认为'r'，reading，只读模式，文件必须存在，否则引发异常。
# todo 另外还有一种模式是'a'，appending。它也是一种写入模式，但你写入的内容不会覆盖之前的内容，而是添加到文件中。
f = file('data/data2.txt', 'w')

# todo 写入内容的方法同样简单：
# todo write的参数可以是一个字符串，或者一个字符串变量。
f.write('a string you want to write')

f.close()
# todo 打开文件还有一种方法，就是open()，用法和file()是一致的。
f = open('data/data2.txt', 'w')
f.write('abcdefgqweqwe')
f.close()

# todo 习题
# todo 1.从一个文件中读出内容，保存至另一个文件。
f = file('data/data2.txt')
data = f.read()
g = file('data/data3.txt', 'w')
g.write(data)
f.close()
g.close()
# todo 2.从控制台输入一些内容，保存至一个文件。
h = file('data/data4.txt', 'w')
some = input("input some else:")
h.write(some)
h.close()

