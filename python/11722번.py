n=int(input())
a=[0]+list(map(int,input().split()))
dp=[0]*(n+1)
dp[0]=0
dp[1]=1
for i in range(2,n+1):
    for j in range(i):
        if a[i]<a[j] and dp[i]<dp[j]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))