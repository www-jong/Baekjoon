import math
N,k=map(int,input().split())
li=[[0]*2 for _ in range(7)]
for _ in range(N):
    S,Y=map(int,input().split())
    li[Y][S]+=1
res=0
for i in range(1,7):
    if li[i][0]<=k:res+=(1 if li[i][0]!=0 else 0)
    else:res+=math.ceil(li[i][0]/k)
    if li[i][1]<=k:res+=(1 if li[i][1]!=0 else 0)
    else:res+=math.ceil(li[i][1]/k)

print(res)