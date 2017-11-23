#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo 在程序运行时，如果我们的代码引发了错误，python就会中断程序，并且输出错误提示。
# todo 在实际的应用中，有很多错误是开发者无法控制的，例如用户输入了一个不合规定的值，或者需要打开的文件不存在。这些情况被称作“异常”，一个好的程序需要能处理可能发生的异常，避免程序因此而中断。

# todo 例如我们去打开一个文件：
# f = file('non-exist.txt')
# print 'File opened!'
# f.close()
# todo 假如这个文件因为某种原因并没有出现在应该出现的文件夹里，程序就会报错：
# todo IOError: [Errno 2] No such file or directory: 'non-exist.txt'
# todo 程序在出错处中断，后面的print不会被执行。
# todo 在python中，可以使用try...except语句来处理异常。做法是，把可能引发异常的语句放在try-块中，把处理异常的语句放在except-块中。
try:
   f = file('non-exist.txt')
   print 'File opened!'
   f.close()
except:
   print 'File not exists.'
print 'Done'
# todo 当程序在try内部打开文件引发异常时，会跳过try中剩下的代码，直接跳转到except中的语句处理异常。于是输出了“File not exists.”。如果文件被顺利打开，则会输出“File opened!”，而不会去执行except中的语句。

# todo 但无论如何，整个程序不会中断，最后的“Done”都会被输出。