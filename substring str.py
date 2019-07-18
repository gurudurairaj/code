d="1234"
i=0
kk=1
j=kk
c=0
ll=0
g=[]
while i<len(d):
    c=0
    while j<=len(d):
        a=d[c:j]
        print(a)
        if a not in g:
            g.append(a)
            if a==a[::-1]:
                ll=ll+1
                #print(a)
        j=j+1
        c=c+1
    kk=kk+1
    j=kk
    i=i+1
print(g,ll)

