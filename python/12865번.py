n,k=map(int,input().split())
dp=[[0]*(k+1) for i in range(n+1)]

for i in range(1,n+1):
    w,v=map(int,input().split())
    for j in range(1,k+1):
        if j<w:dp[i][j]=dp[i-1][j]
        else:dp[i][j]=max(dp[i-1][j-w]+v,dp[i-1][j])
print(dp[n][k])
    
    
    
"""
dp[i][j]=x : i번째 짐에서 무게가 j일때 가치 x
i번째짐을 추가할경우: m은 0부터 k+1까지, dp[i][m]=max(dp[i][m-j]+x,dp[i][m])

"""