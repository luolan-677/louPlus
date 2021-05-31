#! /usr/bin/env python3
N = int(input("please enter a number:"))
sum = 0
count = 0
print("please input {} numbers:".format(N))
while count < N:
    number = float(input())
    sum = sum + number
    count = count + 1
average = sum / N
print("N = {}, sum = {}".format(N,sum))
print("average = {:.2f}".format(average))
xxx
