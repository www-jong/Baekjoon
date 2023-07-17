N=int(input())
li=list(map(int,input().split()))
res=[0]*(N+1)
for i in range(N):
    res=res[:i-li[i]]+[i+1]+res[i-li[i]:]
    
print(*res[:N])