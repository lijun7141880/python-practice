#!/usr/bin/python
# -*- coding: utf-8 -*-
# todo 要读取文件，先得有文件。我们新建个文件，就叫它data.txt。在里面随便写上一些话，保存。把这个文件放在接下来你打算保存代码的文件夹下，这么做是为了方便我们的程序找到它。准备工作就绪，可以来写我们的代码了。

# todo 打开一个文件的命令很简单：file('文件名')
# todo 这里的文件名可以用文件的完整路径，也可以是相对路径。因为我们把要读取的文件和代码放在了同一个文件夹下，所以只需要写它的文件名就够了。
f = file('data/data.txt')

# todo 但这一步只是打开了一个文件，并没有得到其中的内容。变量f保存了这个文件，还需要去读取它的内容。你可以通过read()函数把文件内所有内容读进一个字符串中。
data = f.read()

# todo 输出文件内容
print data

# todo 做完对文件的操作之后，记得用close()关闭文件，释放资源。虽然现在这样一个很短的程序，不做这一步也不会影响运行结果。但养成好习惯，可以避免以后发生莫名的错误。
f.close()

# todo 读取文件内容的方法还有
# todo readline() #读取一行内容
f = file('data/data.txt')
data = f.readline()
print data
f.close()

# todo readlines() #把内容按行读取至一个list中
f = file('data/data.txt')
data = f.readlines()
print data
f.close()