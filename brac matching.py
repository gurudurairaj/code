st=input()
st=list(st)
i=0
l=0
for i in range(len(st)):
    if st[i]=="(" or st[i]==")":
        l=l+1
i=0
j=0
k=0
while i<len(st):
    if len(st)==1:
        break
    if st[i]=="(" :
        while j <len(st):
            if st[j]==")":
                k=k+2
                st.remove(st[i])
                st.remove(st[j-1])
                i=0
            j=j+1
        if  ")" not in st:
            break
         
                
    if st[i]==")":
        while j <len(st):
            if st[j]=="(":
                k=k+2
                st.remove(st[i])
                st.remove(st[j-1])
                i=0
            j=j+1
        if  "(" not in st:
            break
           
    else:
        i=i+1
    j=0
if k==l:
    print("yes")
else:
    print("no")
    
