#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo Python 中函数的参数传递最基本的方式是：
# todo 定义
def func(arg1, arg2):
    print arg1, arg2


# todo 调用
func(3, 7)
# todo 我们把函数定义时的参数名（arg1、arg2）称为形参，调用时提供的参数（3、7）称为实参。
# todo 这种方式是根据调用时提供参数的位置进行匹配，要求实参与行参的数量相等，默认按位置匹配参数。调用时，少参数或者多参数都会引起错误。这是最常用的一种函数定义方式。

# todo 在调用时，也可以根据形参的名称指定实参。如：
func(arg2=3, arg1=7)


# todo Python 语言还提供了其他一些更灵活的参数传递方式，如：
# todo func2(a=1, b=2, c=3)
# todo func3(*args)
# todo func4(**kargs)

# todo 这种方式可以理解为，在一般函数定义的基础上，增加了参数的默认值。这样定义的函数可以和原来一样使用，而当你没有提供足够的参数时，会用默认值作为参数的值。
# todo 例如：
# todo 定义
def func(arg1=1, arg2=2, arg3=3):
    print arg1, arg2, arg3


# todo 调用
func(2, 3, 4)  # 2 3 4
func(5, 6)  # 5 6 3
func(7)  # 7 2 3
# todo 提供的参数会按顺序先匹配前面位置的参数，后面未匹配到的参数使用默认值。

# todo 也可以指定其中的部分参数，如：
func(arg2=8)  # 1 8 3
func(arg3=9, arg1=10)  # 10 2 9

# todo 或者混合起来用：
func(11, arg3=12)  # 11 2 12


# todo 但要注意，没有指定参数名的参数必须在所有指定参数名的参数前面，且参数不能重复。以下的调用都是错误的：
# todo func(arg1=13, 14)
# todo func(15, arg1=16)

# todo 另一种更加灵活的参数传递方式：
# todo def func(*args)  它可以接受任意数量的参数。
def calcSum(*args):
    sum = 0
    for i in args:
        sum += i
    print sum


# todo 调用：
calcSum(1, 2, 3)  # 6
calcSum(123, 456)  # 579
calcSum()  # 0


# todo 在变量前加上星号前缀（*），调用时的参数会存储在一个 tuple（元组）对象中，赋值给形参。在函数内部，需要对参数进行处理时，只要对这个 tuple 类型的形参（这里是 args）进行操作就可以了。因此，函数在定义时并不需要指明参数个数，就可以处理任意参数个数的情况。

# todo 不过有一点需要注意，tuple 是有序的，所以 args 中元素的顺序受到赋值时的影响。如：

def printAll(*args):
    for i in args:
        print i,
    print


# todo 调用：
printAll(1, 2, 3)  # 1 2 3
printAll(3, 2, 1)  # 3 2 1


# todo 虽然3个参数在总体上是相同的，但由于调用的顺序不一样，结果也是不同的


# todo 还有一种更为灵活的参数传递方式：
# todo func(**kargs)  把参数以键值对字典的形式传入。
# todo 示例：
def printAll(**kargs):
    for k in kargs:
        print k, ':', kargs[k]


printAll(a=1, b=2, c=3)  # a:1 c:3 b:2
printAll(x=4, y=5)  # y:5 x:4


# todo 字典是无序的，所以在输出的时候，并不一定按照提供参数的顺序。同样在调用时，参数的顺序无所谓，只要对应合适的形参名就可以了。于是，采用这种参数传递的方法，可以不受参数数量、位置的限制。

# todo Python 的函数调用方式非常灵活，前面所说的几种参数调用方式，可以混合在一起使用。看下面这个例子：
def func(x, y=5, *a, **b):
    print x, y, a, b


func(1)  # 1 5 () {}
func(1, 2)  # 1 2 () {}
func(1, 2, 3)  # 1 2 (3,) {}
func(1, 2, 3, 4)  # 1 2 (3, 4) {}
func(x=1)  # 1 5 () {}
func(x=1, y=1)  # 1 1 () {}
func(x=1, y=1, a=1)  # 1 1 () {'a': 1}
func(x=1, y=1, a=1, b=1)  # 1 1 () {'a': 1, 'b': 1}
func(1, y=1)  # 1 1 () {}
func(1, 2, 3, 4, a=1)  # 1 2 (3, 4) {'a': 1}
func(1, 2, 3, 4, k=1, t=2, o=3)  # 1 2 (3, 4) {'k': 1, 't': 2, 'o': 3}


# todo 在混合使用时，首先要注意函数的写法，必须遵守：
# todo 带有默认值的形参(arg=)须在无默认值的形参(arg)之后；
# todo 元组参数(*args)须在带有默认值的形参(arg=)之后；
# todo 字典参数(**kargs)须在元组参数(*args)之后。

# todo 可以省略某种类型的参数，但仍需保证此顺序规则。

# todo 调用时也需要遵守：
# todo 指定参数名称的参数要在无指定参数名称的参数之后；
# todo 不可以重复传递，即按顺序提供某参数之后，又指定名称传递。

# todo 而在函数被调用时，参数的传递过程为：
# todo 1.按顺序把无指定参数的实参赋值给形参；
# todo 2.把指定参数名称(arg=v)的实参赋值给对应的形参；
# todo 3.将多余的无指定参数的实参打包成一个 tuple 传递给元组参数(*args)；
# todo 4.将多余的指定参数名的实参打包成一个 dict 传递给字典参数(**kargs)。
