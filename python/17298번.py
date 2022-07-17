import sys
input=sys.stdin.readline
n=int(input())
li=list(map(int,input().split()))
ans=[]
idx=0
for i in range(n):
    tmp=0
    while True:
        if idx>=n:
            ans.append(-1)
            idx=i+1
            break
        if li[idx]>li[i]:
            ans.append(li[idx])
            break
        else:
            idx+=1
print(ans)