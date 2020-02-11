point:NameError TypeError 异常处理(try...except) 异常抛出(raise) finally子句
学习python的异常以及如何在代码中处理他们
在程序执行过程中发生的任何错误都是异常，每个异常显示一些相关的错误信息，比如python3中使用python2独有的语法就会发生SyntaxError。

(1)NameError
当访问一个未定义的变量则会发生NameError：
>>> print(kushal)
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
NameError: name 'kushal' is not defined
最后一行包含了错误的详细信息，其余行显示它是如何发生(或什么引起该异常)的详细信息。

(2)TypeError
TypeError也是一种经常出现的异常，当操作或函数应用于不适当类型的对象时引发，一个常见的例子是对整数和字符串做加法。
>>> print(1 + 'kushal')
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: unsupported operaand type(s) for +: 'int' and 'str'

(3)处理异常
我们使用try...except来处理任意异常，基本语法就像这样：
try:
    statements to be inside try clause
    statement2
    statement3
    ...
except ExceptionName:
    statements to evaluated in case of ExceptionName happens
它以如下方式工作：
    首先，执行try子句(在try和except关键字之间的部分)
    如果没有异常发生，except子句在try语句执行完毕后就被忽略了。
    如果在try子句执行过程中发生了异常，那么该子句其余的部分就会被忽略。
    如果异常匹配于except关键字后面指定的异常类型，就执行对应的except子句，然后继续执行try语句之后的代码。
    如果发生了一个异常，在except子句中没有与之匹配的分支，它就会传递到上一级try语句中。
    如果最终仍找不到对应的处理语句，它就成为一个未处理异常，终止程序运行，显示提示信息。
如：
>>> def get_number():
...     "Returns a float number"
...     number = float(input('Enter a float number: '))
...     return number
>>>
>>> while True:
...     try:
...         print(get_number())
...     except ValueError:
...         print('You entered a wrong valus.')
...
Enter a float number: 45.0
45.0
Enter a float number:24,0
You entered a wrong value.
Enter a float number: Traceback (most recent call last):
    File "<stdin>", line 3, in <module>
    File "<stdin>", line 3, in get_number
KeyboardInterrupt
首先输入了一个合适的浮点值，解释器返回输出这个值。
然后输入以逗号分隔的值，抛出valueError异常，except子句捕获，并且打印出错误信息。
第三次按下Ctrl+C，导致了KeyboardInterrupt异常发生，这个异常并未在except块中捕获，因此程序执行被终止。
一个空的except语句能捕获任何异常：
>>> try:
...     input() # 输入的时候按下 Ctrl + C 产生 KeyboardInterrupt
... except:
...     print("Unknown Exception")
...
Unknown Exception

(4)抛出异常
使用raise语句抛出一个异常：
>>> raise ValueError("A value error happened.")
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
ValueError: A value error happened.
可以捕获任何其他普通异常一样，来捕获这些异常：
>>> try:
...    raise ValueError("A value error happened.")
... except ValueError:
...     print("ValueError in our code.")
...
ValueError in our code.

(5)定义清理行为
try语句还有另一个可选的finally子句，目的在于定义在任何情况下都一定要执行的功能，如：
>>> tyr:
...     raise KeyboardInterrupt
... finally:
...     print("Goodbye, world!")
...
Goodbye, world!
KeyboardInterrupt
Traceback (most recent call last):
    File "<stdin>", line 2, in ?
不管有没有发生异常，finally子句在程序离开try后都一定会被执行。
当try语句中发生了未被except捕获的异常(或者它发生在except或else子句中)，在finally子句执行完后它会被重新抛出。
在真实场景的应用程序中，finally子句用于释放外部资源(文件或网络连接之类的)，无论他们的使用过程中是否出错。
