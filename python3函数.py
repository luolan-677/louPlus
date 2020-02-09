函数
(1)定义一个函数
def 函数名(参数)：
    语句1
    语句2
编写一个两个整数求和的函数：
def sum(a,b):
    return a + b
调用方法：
res = sum(234234,34453546464)
res = 34453780698
回文检查：
#! /usr/bin/env python3
def palindrome(s):
    return s == s[::-1]
if __name__ == '__main__':
    s = input('Enter a srting: ')
    if palindrome(s):
        print('Yay a palindrome')
    else:
        print('oh no, not a palindrome')

(2)局域或全局变量
#! /usr/bin/env python3
def change():
    a = 90
    print(a)
a = 9
print('Before the function call',a)
print('inside change function',end=' ')
change()
print('After the function call',a)
# 运行该文件，
./python82.py                                                                                                       [22:44:34]
Before the function call 9
inside change function 90
After the function call 9
在函数里写a = 90时，实际上创建了一个新的名为 a 的局部变量，这个变量只在函数里可用，并且会在函数完成时销毁。
所以即使这两个变量的名字都相同，但是并不是同一个变量。
先定义a，在函数中可以直接使用：
#! /usr/bin/env python3
a = 9
def change():
    print(a)
change()
这边可以直接打印出a = 9
#! /usr/bin/env python3
a = 9
def change():
    print(a)
    a = 100
change()
这样就会报错了，原因是当函数只要用到了变量a，并且a出现在表达式等于号的前面，就会被当成局部变量。
当执行到print(a)的时候会报错，因为a作为函数局部变量是在print(a)之后才定义的。
#! /usr/bin/env python3
a = 9
def change():
    global a
    print(a)
    a = 100
print('Before the function call ',a)
print('inside change function',end=' ')
change() # print(a) 在a = 100前面，所以先打印a = 9，后a = 赋值为100，打印100
print('After the function call ',a)
使用global关键字，对函数中的a标志为全局变量，让函数内部使用全局变量的a，那么整个程序中出现的a都将是全局变量的a。
程序中的end=' '参数表示，print打印后的结尾不用换行，而用空格，默认情况下print打印后会在结尾换行。
#! /usr/bin/env python3
def change():
    dlobal a
    a = 90
    print(a)
a = 9
print('Before the function call ',a)
print('inside change function',end=' ')
change() # a = 90 在print(a)前面，所以运行函数后，会直接将a的值进行改变
print('After the function call ',a)
所以一旦global进行了全局定义，那么内部的a值一旦发生改变，外部的a值也发生了相应的改变。

(3)默认参数值
函数的参数变量可以有默认值，也就是说如果我们对指定的参数变量没有给出任何值就会赋其默认值。
def test(a,b=-99):
    if a > b:
        return True
    else:
        return False
在上面的例子中，我们指明了b的值为-99，如果调用者没有给出b的具体的值，那么b默认的值就是-99。
test(12,23)
False
test(12)
True
重要点1：具有默认值的参数后面不能再有普通参数，如f(a,b=90,c)就是错误的。
重要点2：默认值只能被赋值一次，因此如果默认值是任何可变对象时会有所不同，比如表，字典或大多数类的实例。
例如下方函数，在后续调用的时候会积累前面传给他的参数：
#! /usr/bin/env python3
def f(a,data=[]):
    data.append(a)
    return data
print(f(1))
[1]
print(f(2))
[1,2]
print(f(3))
[1,2,3]
如果要避免这个问题，可以像如下操作：
def f(a,data=None): # 每次循环时，都没有制定data的值，所以data的值一直是none
    if data is None:
        data = []
    data.qppend(a)
    return data
print(f(1))
[1]
print(f(2))
[2]

(4)关键字参数
函数可以通过关键字参数的形式来调用，型如keyword = value：
def func(a,b=5,c=10):
    print('a is',a,'and b is',b,'and c is',c)
func(12,24)
a is 12 and b is 24 and c is 10
func(12,c = 24)
a is 12 and b is 5 and c is 24
func(b = 12,c = 24,a = -1)
a is -1 and b is 12 and c is 24
上面的例子中调用函数时使用了变量名，比如func(12,c = 24)，这样将24赋给c且b具有默认值。

(5)强制关键字参数
def hello(*, name='User'):
    print("Hello", name)
hello('shiyanlou')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: hello() takes 0 positional arguments but 1 was given
hello(name='shiyanlou')
Hello shiyanlou
# 此处存疑

(6)文档字符串
#! /usr/bin/env python3
import math
def longest_side(a,b):
    """
    Function to find the length of the longest side of a right triangle.

    :arg a: Side a of the triangle
    :arg b: Side b of the triangle

    :return: Length of the longest side c as float
    """
    return math.sqrt(a*a + b*b)

if __name__ == '__main__':
    print(longest_side.__doc__)
    print(longest_side(4,5)))
# 存疑

(7-1)高阶函数
高阶函数或仿函数时可以接受函数作为参数的函数：
1.使用一个或多个函数作为参数
2.返回另一个函数作为输出
python里任何函数都能作为高阶函数，例：
# 创建一个函数，将参数列表中每个元素都变成全大写
def high(l):
    return [i.upper() for i in l]
# 创建高阶函数，接受一个函数和一个列表作为参数
def test(h,l):
    return h(l)
l = ['python','Linux','Git']
# 运行高阶函数，返回预期的结果
test(high,l)
['PYTHON','LINUX','GIT']
(7-2)map 函数
map在python中是一个非常有用的高阶函数，接受一个函数和一个序列作为输入，然后对序列的每一个值应用这个函数，返回一个序列，其中包含应用函数后的结果。
lst = [1,2,3,4,5]
def square(num):
    return num * num
print(list(map(square,lst)))
[1,4,9,16,25]
