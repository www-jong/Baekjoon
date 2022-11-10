c=[0,0,0]
li=[]
for i in range(9):
    li.append(list(map(int,input().split())))
for i in range(9):
    for j in range(9):
        if c[0]<li[i][j]:
            c=[li[i][j],i,j]
print("%d\n%d %d"%(c[0],c[1]+1,c[2]+1))