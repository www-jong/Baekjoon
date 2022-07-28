from copy import deepcopy
n,b=map(int,input().split())
li=[]
tmpli=[[] for _ in range(n)]
def mm(x):
    return int(x)%1000
def func(li1,li2):
    tt=0
    for i in range(n):
        tt+=li1[i]*li2[i]
    return tt%1000

for i in range(n):
    li.append(list(map(mm,input().split())))
for i in range(n):
    for j in range(n):
        tmpli[i].append(li[j][i])
ans=deepcopy(li)
for _ in range(b-1):
    for i in range(n):
        for j in range(n):
            tmp=func(li[i],tmpli[j])
            ans[i][j]=tmp
    li=deepcopy(ans)
for i in range(n):
    print(*ans[i])