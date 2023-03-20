N=int(input())
dp=[10**9]*(max(N+1,6))
dp[2]=1
dp[3]=10**9
dp[4]=2
dp[5]=1
for i in range(6,N+1):
    dp[i]=min(dp[i-5]+1,dp[i-2]+1,dp[i-4]+2)
print(dp[N] if dp[N]!=10**9 else -1)