#!/usr/bin/python
# -*- coding: utf-8 -*-
# todo 安装python
# todo 进入Python的官方下载页面Python.org/download，你会看到一堆下载链接。我们就选“Python 2.7.13 Windows Installer”（选最新的即可），如果是64位系统的选下面那个“Python 2.7.13 Windows X86-64 Installer”。如果你不是百分百确定自己是64位系统，请装非64位版本。想用最新 py3 版本也可以
# todo 下载之后，就和装其他软件一样，双击，一路Next，想换安装路径的可以换个位置。但不管换不换，请把这个路径复制下来，比如我的是“C：\python27\”，后面要用到它。另外有个要注意的是，如果有“add python.exe to path”这个选项，请选中它，会让你省不少事。（不同版本这里有差异）
# todo 安装结束还没完，我们还差最后一步：设置环境变量。如果你上一步按照我说的，选上了“add python.exe to path”，则可略过此步骤。这是什么东西我暂时先不解释，大家照着做就好。右键单击我的电脑，依次点击"属性"->"高级"->"环境变量"，在“系统变量”表单中点击叫做Path的变量，然后编辑这个变量，把“;C:\Python27\”，也就是你刚才复制的安装路径，加到它的结尾。注意！要用英文分号和前面已有的内容隔开。然后点确定，点确定，再点确定。完成。
# todo 注意1：win7系统是右键单击“计算机”，点击“属性”->“高级系统设置”->“环境变量”
# todo 注意2：win10系统需要在Path里新建一条记录，把路径加进去，无需分号
# todo 注意3：环境变量里会有用户变量和系统变量两类，如果添加后无效，建议在两类的Path里都加上路径，或者尝试重启下系统
# todo 注意4：设置完要重新打开命令行
# todo 怎么知道你已经成功安装了Python呢？这时候你需要打开命令行，或者叫命令提示符、控制台。方法是：点击开始菜单->程序->附件->命令提示符；或者直接在桌面按快捷键“Win+r”，Win键就是Ctrl和Alt旁边那个有windows图标的键，输入cmd，回车。这时候你就看到黑底白字了。

# todo 在命令行里输入python，回车。如果看到诸如：Python 2.7.5 (default, May 15 2013, 22:43:36) [MSC v.1500 32 bit (Intel)] on win32的提示文字，恭喜你！否则，请重新检查你哪里的打开方式不对。