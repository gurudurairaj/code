matrix=[[1,2,3,4],
        [5,200,7,8],
        [9,10,11,12],
        [13,14,15,15]]
m=0
n=0
rot=0
d=1
r=1
ro=len(matrix)-1
c=len(matrix[0])-1
#print(r,c)
while rot<r:
    while d>=1:
        temp=matrix[m][n]
        print(m,n,ro,c)
        for i in range(m,c):
            matrix[m][i]=matrix[m][i+1]
        for i in range(n,ro):
            matrix[i][c]=matrix[i+1][c]
        for i in range(c,m,-1):
            matrix[ro][i]=matrix[ro][i-1]
        for i in range(ro,m,-1):
            matrix[i][n]=matrix[i-1][n]
        matrix[m+1][n]=temp
        print(m,n,temp)
        m=m+1
        n=n+1
        ro=ro-1
        c=c-1
        if ro-m<0 or c-n<0:
            m,n=0,0
            ro,c=len(matrix)-1,len(matrix[0])-1
            print("q")
            break
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print(matrix[i][j],end=" ")
            print()
    rot=rot+1
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j],end=" ")
    print()
