def sub(q,w,e,z):
    q.append(w)
    for i in range(z,len(e)):
        w.append(e[i])
        sub(q,w,e,i+1)
        del w[len(w)-1]
    print(q[0])
a=[1,2,3,4,5]
s=[]
c=[]
sub(s,c,a,0) 
