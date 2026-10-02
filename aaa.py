#!/usr/bin/python3
from sys import stdin
a=[]
for i in stdin:
    a.append(i[:-1])
l=sorted(a, reverse=True)
print(l)
for i in l:
    print(i)


