N,X=map(int,input().split())
li=list(map(int,input().split()))
res=10**10
for i in range(N-1):
    res=min(res,li[i]*X+li[i+1]*X)
print(res)