#!/usr/bin/python3
import random
l=int(input())
matdna=[]
nucl=['A','T','C','G']
for i in range (l):
    matdna.append(random.choice(nucl))
print(matdna)

