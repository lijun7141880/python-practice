#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo 有时候，仅仅代入一个值不能满足我们构造字符串的需要。
# todo 例如
# todo Mike‘s score is 87.
# todo Lily‘s score is 95.
# todo 在python中，你可以这样实现：
# todo print "%s's score is %d" % ('Mike', 87)
# todo 或者
# todo name = ‘Lily’
# todo score = 95
# todo print "%s's score is %d" % (name, score)
# todo 无论你有多少个值需要代入字符串中进行格式化，只需要在字符串中的合适位置用对应格式的%表示，然后在后面的括号中按顺序提供代入的值就可以了。占位的%和括号中的值在数量上必须相等，类型也要匹配。
# todo ('Mike', 87)这种用()表示的一组数据在python中被称为元组（tuple），是python的一种基本数据结构
