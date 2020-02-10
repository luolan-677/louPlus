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
''
