n=int(input())
g=[0]*(501)
for i in range(n):
    a,b=map(int,input().split())
    g[a]=b
dp=[0]*(500+1)
dp[0]=0
for i in range(1,500+1):
    if g[i]==0:
        continue
    for j in range(i):
        if g[j]<g[i] and dp[i]<dp[j]:
            dp[i]=dp[j]
    dp[i]+=1
print(n-max(dp))
