n,m=map(int,input().split())
A=list(map(int,input().split()))
C=list(map(int,input().split()))
dp=[[0 for _ in range(sum(C)+1)] for _ in range(n+1)]
res=sum(C)
for i in range(1,n):
    for j in range(1,sum(C)+1):
        if j<C[i]:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(A[i]+dp[i-1][j-C[i]],dp[i-1][j])
        if dp[i][j]>=m:
            res=min(res,dp[i][j])
print(res)