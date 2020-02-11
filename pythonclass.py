python 类
在python中，所有数据类型都可以视为对象，当然也可以自定义对象。
自定义的对象数据类型就是面向对象中的类(class)的概念。
point：类的定义 对象初始化

(1)定义类
类的语法：
class nameoftheclass(parent_class):
    statement1
    statement2
    statement3
在类的声明中可以写任何python语句，包括定义函数(在类中称为方法)
>>> class MyClass(object):
        """A simple example class"""
        i = 12345
        def f(self):
            return 'hello world'

(2)\init__方法
类的实例化使用函数符号。
只要将类对象看作是一个返回新的类实例的无参数函数即可：
x = Myclass()
以上创建了一个新的类实例并将该对象赋给局部变量x。
这个实例化操作创建了一个空的对象。
很多类都倾向于将对象创建为有初始状态的。
因此类可能会定义一个名为__init__()的特殊方法，如下：
def __init__(self):
    self.data = []
类定义了__init__()方法的话，类的实例化操作会自动为创建的类实例调用__init__()方法。
所以在下例中，可以这样创建一个新的实例：
x = Myclass
当然，处于弹性的需要，__init__()方法可以有参数。
事实上，参数通过__init__()传递到类的实例化操作上，如：
>>> class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
...
>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)

(3)继承
当一个类继承另一个类时，它将继承父类的所有功能(如变量和方法)。
这有助于重用代码。
首先创建一个叫做Person的类，然后创建两个派生类Student和Teacher。
当两个类都从Person类继承时，它们的类除了会有Person类的所有方法还会有自身用途的新方法和新变量。
student_teacher.py
代码如下：
#! /usr/bin/env python3
class Person(object):
    """
    返回具有给定名称的Person对象
    """

    def __init__(self, name):
        self.name = name

    def get_details(self):
        """
        返回包含人名的字符串
        """
        return self.name

class Student(Person):
    """
    返回Student对象，采用name，branch，year 3个参数
    """

    def __init__(self, name, branch, year):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year

    def get_details(self):
        """
        返回包含学生具体信息的字符串
        """
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)

class Teacher(Person):
    """
    返回teacher对象，采用字符串列表作为参数
    """
    def __init__(self, name, papers):
        Person.__init__(self, name)
        self.papers = papers

    def get_details(self) :
        return "{} teachers {}".format(self.name, ','.join(self.papers))

person1 = Person('Sachin')
student1 = Student('Kushal', 'CSE', 2005)
teacher1 = Teacher('Prashad', ['C', 'C++'])

print(person1.get_details())
print(student1.get_details())
print(teacher1.get_details())
----------结果----------
Sachin
Kushal studies CSE and is in 2005 year.
Prashad teachers C,C++
在上述例子中，可以看到怎样在student类和teacher类中调用person类的__init__方法。
也在student类和teacher类中重写了person类的get_details()方法。
因此，调用Student1和Teacher1的get_details()方法时，使用的是各自类(student和teacher)中定义的方法。

(4)多继承
一个类可以继承自多个类，具有父类的所有变量和方法，语法如下：
class MyClass(Parentclass1, Parentclass2, ...):
    def __init__(self):
        Parentclass1.__init__(self)
        Parentclass2.__init__(self)
        ...
        ...

(5)删除对象
已经知道了如何创建对象，现在学习怎样删除一个对象，使用关键字del来进行操作。
>>> s = "I love you"
>>> del s
>>> s
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 's' is not defined
del实际上使对象的引用计数减少一，当对象的引用计数变成零的时候，垃圾回收器会删除这个对象。

(6)属性attributes读取方法
在python中直接使用属性就可以了：
>>> calss Student(object):
        def __init__(self, name):
            self.name = name
...
>>> std = Student("Kushal Das")
>>> print(std.name)
Kushal Das
>>> std.name = "Python"
>>> print(std.name)
Python

(7)装饰器
想要更加精确的调整控制属性访问权限，可以使用@property装饰器，@property装饰器就是负责把一个方法变成属性条用的。
例：银行账号，确保没有人能设置金额为负数，并且有个只读属性cny返回换算人民币后的金额。
#! /usr/bin/env python3
class Account(object):
    """账号类，
    amount 是美元金额.
    """
    def __init__(self, rate):
        self.__amt = 0
        self.rate = rate

    @property
    def amount(self):
        """账号余额(美元)"""
        return self.__amt

    @property
    def cny(self):
        """账号余额(人民币)"""
        return self.__amt * self.rate

    @amount.setter
    def amount(self, value):
        if value < 0:
            print("Sorry, no negative amount in the account.")
            return
        self.__amt = value

if __name__ == '__mian__':
    acc = Account(rate=6.6) # 基于课程编写时的汇率
    acc.amount = 20
    print("Dollar amount:", acc.amount)
    print("In CNY:", acc.cny)
    acc.amount = -100
    print("Dollar amount", acc.amount)
----------结果----------
Dollar amount: 20
In CNY: 132.0
Sorry, no negative amount in the account.
Dollar amount: 20
