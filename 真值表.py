#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo 逻辑判断是编程中极为常用的知识。
# todo 这种被称为“真值表”的东西，罗列了基本逻辑运算的结果。
# todo <=>来表示等价关系。
# todo <=>左边表示逻辑表达式，<=>右边表示它的结果。

# NOT
# not False <=> True
# not True <=> False
# （not的结果与原值相反）
#
# OR
# True or False <=> True
# True or True <=> True
# False or True <=> True
# False or False <=> False
# （只要有一个值为True，or的结果就是True）
#
# AND
# True and False <=> False
# True and True <=> True
# False and True <=> False
# False and False <=> False
# （只要有一个值为False，and的结果就是False）
#
# NOT OR
# not (True or False) <=> False
# not (True or True) <=> False
# not (False or True) <=> False
# not (False or False) <=> True
#
# NOT AND
# not (True and False) <=> True
# not (True and True) <=> False
# not (False and True) <=> True
# not (False and False) <=> True
#
# !=
# 1 != 0 <=> True
# 1 != 1 <=> False
# 0 != 1 <=> True
# 0 != 0 <=> False
#
# ==
# 1 == 0 <=> False
# 1 == 1 <=> True
# 0 == 1 <=> False
# 0 == 0 <=> True
