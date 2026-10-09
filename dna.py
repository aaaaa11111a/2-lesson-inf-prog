#!/usr/bin/python3
import random
l=int(input())
dna=[]
for i in range (l):
    nucl=random.choice('ATGC')
    dna.append(nucl)
matdna=''.join(dna)
with open ('dna.txt','w') as file:
    file.write(matdna)

