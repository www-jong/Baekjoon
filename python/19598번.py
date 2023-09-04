import sys
input=sys.stdin.readline
N=int(input())
li=[]
for i in range(N):
    a,b=map(int,input().split())
    li.append([a,b])
li.sort(key=lambda x:(x[0],-x[1]))
res=[0]
for i in range(N):
    idx=0
    ch=0
    while idx<len(res):
        if res[idx]<=li[i][0]:
            res[idx]=li[i][1]
            ch=1
            break
        idx+=1
    if not ch:
        res.append(li[i][1])
print(len(res))