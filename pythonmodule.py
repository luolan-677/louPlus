python模块
point：模块的导入 包 默认/第三方模块介绍 命令行参数
(1)模块
到目前为止，在Python解释器中写的所有代码都在我们退出解释器的时候丢失了。
但是当人们编写大型程序的时候他们会倾向于将代码分为多个不同的文件以便使用，调试及拥有更好的可读性。
在python中我们使用模块来达到这些目的。
模块是包括python定义和声明的文件，文件名就是模块名加上.py后缀。
你可以由全局变量 __name__ 得到模块的模块名(一个字符串)。
现在我们来看看模块是怎样工作的，首先创建一个bars.py文件，内容如下：
"""
Bars Module
============
这是一个打印不同分割线的示例模块
"""
def starbar(num):
    """打印 × 分割线

    :arg num: 线长
    """
    print('*' * num)

def hashbar(num):
    """打印 # 分割线

    :arg num: 线长
    """
    print('#' * num)

def simplebar(num):
    """打印 - 分割线

    :arg num: 线长
    """
    print('-' * num)
现在我们启动解释器然后导入我们的模块：
>>> import bars
>>>
我们必须使用模块名来访问模块内的函数：
>>> bars.hashbar(10)
##########
>>> bars.simplebar(10)
----------
>>> bars.starbar(10)
**********
导入模块：
有不同的方式导入模块，已经看到了一种，甚至可以从模块中导入指定的函数，如：
>>> from bars import simplebar, starbar
>>> simplebar(20)
--------------------
当然还可以用from module import * 导入模块中的所有定义，然而这并不是推荐的做法。

(2)包
含有 __init__.py 文件的目录可以用来作为一个包，目录里的所有.py文件都是这个包的子模块。
创建mymodule目录，目录结构如下：
tree mymodule
mymodule
|----bars.py
|----__init__.py
|----utils.py
在这个例子中，mymodule是一个包名并且bars和utils是里面的两个子模块。
首先创建mymodule目录：
mkdir mymodule
然后将上一节编写的bars.py拷贝到mymodule目录下，然后可以使用touch创建一个空的__init__.py文件。
使用touch命令创建一个空的__init__.py文件。
如果__init__.py文件内有一个名为__all__的列表，那么只有在列表内列出的名字将被公开。
如果mymodule内的__init__.py文件含有以下内用：
from mymodule.bars import simplebar
__all__ = [simplebar, ]
那么导入时将只有simplebar可用，如果在python3解释器中进行测试，需要确定是在mymodule目录同级的目录下执行的python3。
类似下面的操作，否则会出现ImportError: No module named 'mymodule'的报错。
cd /home/shiyanlou
python3
注：from mymodule import * 只能工作在模块级别的对象上，试图导入函数或类将导致syntax error。

(3)默认模块
安装python的时候会附带安装不同的模块，可以按需使用它们，也可以为其他特殊用途安装新模块。
>>> modules # 即可查看所有已安装的模块情况
也可以通过关键字查询对应的模块/类的文档，如：
>>> help(str)

(4)os 模块
os 模块提供了与操作系统相关的功能，可以使用如下语句导入：
>>> import os
getuid()函数返回当前进程的有效用户id：
>>> os.getuid()
500
getpid()函数返回当前进程的id，getppid()返回父进程的id：
>>> os.getpid()
16150
>>> os.getppid()
14847
uname()函数返回识别操作系统的不同信息，在linux中他返回的详细信息可以从uname -a命令得到。
uname()返回的对象是一个元祖，(sysname, nodename, relese, version, machine)。
>>> os.uname()
('Linux', 'd80', '2.6.34.7-56.fc13.i686.PAE', '#1 SMP Wed Sep 15 03:27:15 UTC 2010', 'i686')
getcwd()函数返回当前工作目录。chdir(path)则是更改当前目录到path。
在例子中我们首先看到当前工作目录是/home/shiyanlou，然后我们更改当前工作目录到/Code并再一次查看当前工作目录。
>>> os.getcwd()
'/home/shiyanlou'
>>> os.chdir('Code')
>>> os.getcwd()
'/home/shiyanlou/Code'
所以现在让我们使用os模块提供的另一个函数来创建一个自己的函数，它将列出给定目录下的所有文件和目录。
def view_dir(path='.'):
    """
    这个函数打印给定目录中的所有文件和目录
    :args path: 指定目录，默认为当前目录
    """
    names = os.listdir(path)
    names.sort()
    for name is names:
        print(name, end = ' ')
    print()
使用例子中的view_dir()函数：
>>> view_dir('/')
.bashrc .dockerenv .profile bin boot dev etc home lib lib64 media mnt opt proc root run sbin srv sys tmp usr var
os模块中还有许多非常有用的函数，详情https://docs.python.org/3/library/os.html。

(5)requests模块
(5-1)requests是一个第三方python的模块
第三方模块并不是默认的模块，是要安装后才能进行使用，使用pip3进行安装：
sudo apt-get update
sudo apt-get install python3-pip
然后用pip3安装requests
sudo pip3 install requests
上面的命令会在你的系统中安装python3版本的requests模块。
(5-2)获得一个简单的网页
可以使用get()方法获取任意一个网页
>>> import requests
>>> req = requests.get('https://github.com')
>>> req.status_code
200
req的text属性存有服务器返回的HTML网页，由于HTML文本太长就不进行展示。
使用这个知识，写一个能够从制定的URL中下载文件的程序：
#! /usr/bin/env python3
import requests
def download(url)
    """
    从指定的URL中下载文件并存储到当前目录
    url: 要下载页面内容的网址
    """
    # 检查URL是否存在
    try:
        req = requests.get(url)
    except requests.exceptions.MissingSchema:
        print('Invalid URL "{}"'.format(url))
        return
    # 检查是否成功访问了该网站
    if req.status_code == 403:
        print('You do not have the authority to access this page.')
        return
    filename = url.split('/')[-1]
    with open(filename, 'w') as fobj:
        fobj.write(req.content.decode('utf-8'))
    print("Download over.")

if __name__ == '__main__':
    url = imput('Enter a URL: ')
    download(url)
程序测试，已经完成一个文件的下载。
注意到：if __name__ == '__mian__'这条语句：
作用：只有存在当前模块名为__main__的时候(即作为脚本执行的时候)才会执行此 if 块内的语句。
换句话说，当此文件以模块的形式导入到其他文件中时，if 块内的语句并不会执行。

(6)argparse命令行参数处理模块
这里用到的模块是sys，命令行传入的所有参数都可以使用sys.argv获取，如果希望对参数进行处理可以说会用argparse模块：
https://docs.python.org/3/howto/argparse.html

(7)tab补全
首先创建一个文件：~/.pythonrc，文件内写入如下内容：
import rlcompleter, readline
readline.parse_and_blid('tab: complete')

history_file = os.path.expanduser('~/.python_history')
readline.read_history_file(history_file)

import atexit
atexit.register(readline.write_history_file, history_file)
下一步在~/.bashrc文件中设置PYTHONSTARTUP环境变量指向这个文件：
$ export PYTHONSTARTUPA=~/.pythonrc
现在，从今以后每当你打开bash shell，你将会拥有TAB补全和Python解释器中代码输入的历史记录。
要在当前shell中使用，source这个bashrc文件。
$ source ~/.bsahrc

python官方文档：https://docs.python.org/3/library/index.html
python第三方模块：https://pypi.org/
