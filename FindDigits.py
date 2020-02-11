#! /usr/bin/env python3
fobj = open('/tmp/String.txt')
s = fobj.read()
res = ''

for char in s:
    if char.isdigit():
        res += char
print(res)
