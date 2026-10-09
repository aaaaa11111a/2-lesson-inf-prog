a=int(input())
l=[]
d=2
while a!=1:
    while a%d==0:
        a=a//d
        l.append(d)
    d+=1
print(l)
