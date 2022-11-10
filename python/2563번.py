li=[[0]*(101) for i in range(101)]
N=int(input())
for i in range(N):
    a,b=map(int,input().split())
    for i in range(a,10+a):
        for j in range(b,10+b):
            li[i][j]=1
ans=0
for i in range(101):
    ans+=sum(li[i])
print(ans)