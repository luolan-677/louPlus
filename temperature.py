#! /usr/bin/env python3
fahrenheit = float(input("please enter a fahrenheit: "))
celsius = (fahrenheit - 32) / 1.8 # 转化为摄氏度
print("{:5.2f}{:7.2f}".format(fahrenheit,celsius))
