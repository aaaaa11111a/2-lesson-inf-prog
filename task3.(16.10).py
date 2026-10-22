import string
file='/usr/share/licenses/imhex/LICENSE'
with open(file,'r') as file:
    text=file.read()

for i in string.punctuation:
    text=text.replace(i,' ')
text=text.lower()
words=text.split()
wcount={}
for i in words:
    if i in wcount:
        wcount[i]+=1
    else:
        wcount[i]=1
sortwords=sorted(wcount,key=wcount.get, reverse=True)
for i in range (10):
    word=sortwords[i]
    count=wcount[word]
    print(f"{i+1}.{word}: {count}")



