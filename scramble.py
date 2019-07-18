from random import shuffle
f=open("red.txt","r")
s=f.read()
d="u"
k="'"
h=[]
for i in range(len(s)):
    if s[i].isalpha() or s[i]=='"' or s[i]=="'":
        d=d+s[i]
    else:
        h.append(d)
        d="u"
    if i==len(s)-1:
        h.append(d)
    if s[i]=='.':
        h.append(s[i])
for i in range(len(h)):
    h[i]=h[i].replace("u","")
m=len(h)
print(h)
for i in range(len(h)):
    r=h[i]
    if k in r:
         for hy in range(len(r)):
             if r[hy]=="'":
                 p=hy
         r=list(r)
         shuffle(r)
         b=''.join(r)
         b=b.replace("'","")
         b=list(b)
         b.insert(p,k)
         bk=''.join(b)
         h.append(bk)
         
    elif r[0]!='"':
        r=list(r)
        shuffle(r)
        b=''.join(r)
        h.append(b)
    else:
        h.append(r)
h[m]=h[0]
h[len(h)-1]=h[m-1]
for i in range(m,len(h)):
    print(h[i],end=" ")
    
