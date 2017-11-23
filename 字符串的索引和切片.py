#!/usr/bin/python
# -*- coding: utf-8 -*-
# todo 字符串的一些与list相似的操作
# todo 1. 遍历
# todo 通过for...in可以遍历字符串中的每一个字符。
word = 'helloworld'
for c in word:
   print c

# todo 2. 索引访问
# todo 通过[]加索引的方式，访问字符串中的某个字符。
print word[0]
print word[-2]
# todo 与list不同的是，字符串不能通过索引访问去更改其中的字符。
# todo todo word[1] = 'a'
# todo 这样的赋值是错误的。

# todo 3. 切片
# todo 通过两个参数，截取一段子串，具体规则和list相同。
print word[5:7]
print word[:-5]
print word[:]

# todo 4. 连接字符
# todo join方法也可以对字符串使用，作用就是用连接符把字符串中的每个字符重新连接成一个新字符串。
newword = ','.join(word)
print newword