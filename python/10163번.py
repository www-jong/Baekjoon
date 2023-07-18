N=int(input())
res=[0]*(N)
li=[[0]*(1001) for i in range(1001)]
squ=[]
for i in range(N):
    x1,y1,w,h=map(int,input().split())
    squ.append([x1,y1,w,h])

idx=0
for x1,y1,w,h in squ[::-1]:
    tmp=0
    for x in range(x1,x1+w):
        for y in range(y1,y1+h):
            if li[x][y]==0:
                tmp+=1
                li[x][y]=1
    res[idx]=tmp
    idx+=1
print(*res[::-1],sep="\n")