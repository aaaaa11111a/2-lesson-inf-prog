import random
l=int(input())
file='genbred.txt'
with open(file,'r',encoding='utf-8') as file:
    text=file.read()
text=text.lower()
punct='.,?!:;-'
for _ in punct:
    text=text.replace(_,' ')
words=text.split()
if len(words)<2:
    print('Недостаточно слов')
else:
    a={}
    for i in range(len(words)-1):
        w1=words[i]
        w2=words[i+1]
        if w1 not in a:
            a[w1]=set()
            a[w1].add(w2)
    output=[]
    w1=random.choice(list(a.keys()))
    output.append(w1)
    for i in range(l-1):
        if w1 in a and a[w1]:
            w2=random.choice(list(a[w1]))
            output.append(w2)
            w1=w2
        else:
            w1=random.choice(list(a.keys()))
            output.append(w1)
    final=' '.join(output)
    print(final)
