di=["he","is","my","hero","and"]
a=input()
d={}
for i in range(len(di)):
    if a.find(di[i])==-1:
        pass
    else:
        print(di[i])
        d[di[i]]=a.find(di[i])
print(d)

        
