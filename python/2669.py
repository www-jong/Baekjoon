li=[[0]*(101) for i in range(101)]
res=0
for i in range(4):
    x1,y1,x2,y2=map(int,input().split())
    for x in range(x1,x2):
        for y in range(y1,y2):
            if li[x][y]==0:
                li[x][y]=1
                res+=1

print(res)


