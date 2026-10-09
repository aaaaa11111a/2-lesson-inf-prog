#!/usr/bin/python3
with open('dna.txt','r') as file:
    matdna=file.read().strip()
for nucl in 'ATGC':
    print(f" {nucl}:{matdna.count(nucl)}")
compdna=matdna.replace('A','t').replace('T','a').replace('G','c').replace('C','g')
compdna=compdna.upper()
print(compdna)
dnapart=input()
position=[]
for i in range (len(matdna)-len(dnapart)+1):
    if matdna[i:i+len(dnapart)]==dnapart:
        position.append(i)
if position:
    print('Найдено на позициях:',','.join(map(str,position)))
else:
    print('Вхождений не найдено')
