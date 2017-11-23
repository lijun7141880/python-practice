#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo 将数据转成文本的过程又被称为“序列化”，即将对象状态转换为可保持或传输的格式的过程。对应的，从序列化的格式中解析对象状态的过程被称为“反序列化”。
# todo  pickle。它可以把任何 Python 对象存储在文件中，再把它原样取出来。

# todo 存储的过程：
import pickle
test_data = ['Save me!', 123.456, True]
f = file('test.data', 'w')
pickle.dump(test_data, f)
f.close()
# todo 这样，我们就把 test_data 这个 list 存储在了文件 test.data 中。

# todo 存储的过程：
import pickle
f = file('test.data')
test_data = pickle.load(f)
f.close()
print test_data
# todo 控制台的输出：  ['Save me!', 123.456, True]
# todo 和存储前的数据是一致的。

# todo Python 还提供了另一个模块 cPickle，它的功能及用法和 pickle 模块完全相同，只不过它是用C语言编写的，因此要快得多（比pickle快1000倍）。因此你可以把上述代码中的 pickle 全部替换为 cPickle，从而提高运行速度（尽管在这个小程序中影响微乎其微）。