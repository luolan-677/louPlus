python3文件处理
(1)文件打开
使用open()函数打开文件，需要两个参数，第一个参数是文件路径或者文件名，第二个参数是打开模式，如下：
'r' 以只读模式打开，只能读取文件内容，不能进行编辑或者删除。
'w' 以写入模式打开，如果文件存在则会删除文件里面的所有内容，然后打开这个文件进行写入。
'a' 以追加模式打开，写入到文件中的任何数据都会自动追加到末尾。
默认模式为只读模式，不进行指定的话，open()函数会以只读模式打开文件。
wget http://labfile.oss.aliyuncs.com/courses/596/sample.txt
fobj = open('sample.txt')
fobj
<_io.TextIOWrapper name='sample.txt' mode='r' encoding='UTF-8'>

(2)文件关闭
打开文件使用完毕后，需要将文件进行关闭，命令如下：
fobj.close()
始终需要确保关闭每一个打开的文件，程序能打开的文件数量有限，一旦超过这个限制可能会导致程序崩溃，从而造成数据的丢失。

(3)文件读取
----------函数：read()----------
使用read()方法一次性读取整个文件：
fobj = open('sample.txt')
fobj.read()
'I love Python\nI love shiyanlou\n'
fobj.close()
如果再一次调用read()，它会返回空字符串，因为已经完整的读取了整个文件，如下：
fobj = open('sample.txt')
fobj.read()
'I love Python\nI love shiyanlou\n'
fobj.read()
' ' # 因为已经读取过一次，所以这边再次进行读取操作时，就无法读取到内容。
read(size)有一个可选的参数size，用于指定字符串的长度，如果没有指定size或者指定为负数，就会读取并返回整个文件。
当文件大小为当前机器内存两倍时，就会产生问题，反之，会尽可能按比较大的size读取和返回数据。
----------函数：readline()----------
每次读取文件中的一行。
fobj = open("sample.txt")
fobj.readline()
'I love Python\n'
fobj.readline()
'I love shiyanlou\n'
fobj.close()
----------函数：readlines()----------
用readlines()函数可以将所有行读取到一个列表中。
fobj = open('sample.txt')
fobj.readlines()
['I love Python\n', 'I love shiyanlou\n']
fobj.close()
也可以用循环遍历文件对象来读取文件中的每一行：
fobj = open('sample.txt')
for x in fobj:
    print(x,end = '')
I love Python
I love shiyanlou
fobj.close()
例：写一个程序，将用户输入的字符串作为将要读取文件的文件名，并将文件内容打印在屏幕上。
#! /usr/bin/env python3
name = input('Enter the file name: ')
fobj = open(name)
print(fobj.read())
fobj.close()

(4)文件写入
----------函数：write()----------
使用write()方法打开一个文件然后随便写入一些文本
fobj = open('ircnicks.txt','w')
fobj.write('powerpork\n')
fobj.write('indrag\n')
fobj.write('mishti\n')
fobj.write('sankarshan')
fobj.clouse()
结果：
fobj = open('ircnicks.txt')
s = fobj.read()
print(s)
powerpork
indrag
mishti
sankarshan
fobj.close()

(5)拷贝文件
拷贝指定的文本文件到另一个指定的文本文件。
#! /usr/bin/env python3
import sys
if len(sys.argv) < 3:
    print('Wrong parameter')
    print('./copyfile.py file1 file2')
    sys.exit(1)
f1 = open(sys.argv[1])
s = f1.read()
f1.close()
f2 = open(sys.argv[2],'w')
f2.write(s)
f2.close()
这里使用了一个新模块sys。
sys.argv包含所有命令行参数，这个程序的功能完全可以使用shell的cp命令替代。
sys.argv的第一个值是命令自身的名字，下面这个程序打印命令行参数：
#! /usr/bin/env python3
import sys
print('First value',sys.argv[0])
print('All values')
for i,x in enumerate(sys.argv):
    print(i,x)
----------结果----------
./argvtest.py Hi there
First value ./argvtest.py
All values
0 ./argvtest.py
1 Hi
2 there
这里用到了一个新的函数enumerate(iterableobject)，在序列中循环时，索引位置和对应值可以使用它同时得到。
sys函数存疑----------

(6)文本文件相关信息统计
写一个程序，对任意给定文本文件中的制表符，行，空格进行计数。
#! /usr/bin/env python3
import os
import sys
def parse_file(path):
    """
    分析给定文本文件，返回其空格，制表符，行的相关信息

    :ard path: 要分析的文本文件的路径

    :return: 包含空格数，制表符数，行数的元组
    """
    fd = open(path)
    i = 0
    spaces = 0
    tabs = 0
    for i,line in enumerate(fd):
        spaces += line.count(' ')
        tabs += line.count('\t')
    # 现在关闭打开的文件
    fd.close()

    # 以元组形式返回结果
    return spaces,tabs,i + 1

def main(path):
    """
    函数用于打印文件分析结果

    :arg path: 要分析的文本文件的路径
    :return: 若文件存在则为 True，否则 False
    """
    if os.path.exists(path):
        spaces,tabs,lines = parse_file(path)
        print("Spaces {}. tabs {}. lines {}".format(spaces,tabs,lines))
        return True
    else:
        return False

if __name__== '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        sys.exit(-1)
    sys.exit(0)
----------结果----------
./parsefile.py sample.txt
Spaces 4. tabs 0. lines 2
程序有两个函数，main()和parse_file()，parse_file函数真正的文件文件并返回结果，然后在main()函数里打印结果。

(7)使用with语句
在实际情况中，我们应该尝试使用with语句处理文件对象，它会在文件用完后会自动关闭，就算发生异常也没有关系，如下：
with open('sample.txt') as fobj:
    for line in fobj:
        print(line,end = '')
----------结果----------
I love Python
I love shiyanlou

(8)实现lscpu命令
lscpu命令是读取/proc/cpuinfo这个文件的信息并美化输出，写一个python程序以只读模式读取/proc/cpuinfo这个文件，然后进行打印。
一定要记得一行一行读取文件，不能一次性读取文件，有时候读取的文件大小可能超过了电脑内存。
#! /usr/bin/env python3
with open('/proc/cpuinfo','r') as cpuinfo:
    for line in cpuinfo:
        print(line,end='')
