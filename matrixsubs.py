s=[(1,2,3,4,5,6,7,8,9,0),(  
0,9,8,7,6,5,4,3,2,1),(  
1,1,1,1,1,1,1,1,1,1 ),( 
1,1,1,1,1,1,1,1,1,1  ),(
2,2,2,2,2,2,2,2,2,2, )]
st=[(8,7,6,5,4,3),(  
1,1,1,1,1,1),(  
1,1,1,1,1,1)]
stt=[]
for i in range(len(st)):
    for j in range(len(st[0])):
        stt.append(st[i][j])
c=0
m=len(st)
n=len(st[0])
ks=0
g=n-1  
p=0
lo=0
q=0
w=0
for i in range(len(s)):
    for j in range(len(s)):
        print(s[i][j],end="")
    print("")
for i in range(len(s)-m+1):
    a=i
    for j in range(len(s[0])-n+1):
        for k in range(m*n):
            #print(a,ks)
            if s[a][ks]==stt[q]:
                c=c+1
            if ks==g:
                ks=p-1
                a=a+1
            ks=ks+1
            q=q+1
        p=p+1
        ks=p
        a=i
        g=g+1
        q=0
        #print("c",c)
        if c==m*n:
            lo=lo+1
            #print()
            print("possible")
            #print()
            c=0
          
        c=0
    c=0
    q=0
    ks=0
    g=n-1
    p=0
    
 

