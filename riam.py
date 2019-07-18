g=[[1,1,1,1,1],
   [0,0,1,0,0],
   [1,1,1,1,1],
   [1,0,1,1,1],
   [0,0,1,1,1]]
print("right","down")
for i in range(5):
    for j in range(5):
        print(g[i][j],end="")
    print("")
def rat(f,i,j):
    if f[0][0]==1 and f[4][4]==1 and i<5 and j<5 and i>=0 and j>=0:
        if f[i][j]==1:
            rat(f,i,j+1)
            rat(f,i+1,j)
            #rat(f,i,j-1)
            if i==4 and j==4:
                print("s")
rat(g,i=0,j=0)
