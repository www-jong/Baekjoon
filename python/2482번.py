import sys
input=sys.stdin.readline

N=int(input())
K=int(input())
dp=[[[0,0]for i in range(K+1)] for _ in range(N+1)]
# dp[i][j]= i번째색상에서 j개색조합 가능한 수
# dp[i[j][0]= i번째 색상을 고르지 않았을 때 j개 구성수
for i in range(N+1):
    dp[i][1][1]=1
    dp[i][1][0]=max(i-1,0)
    dp[i][0][0]=1
for i in range(2,N):
    for j in range(2,min(i+1,K+1)):
        dp[i][j][0]=sum(dp[i-1][j])%1000000003
        dp[i][j][1]=(dp[i-2][j-1][0])%1000000003
for i in range(1,K+1):
    dp[N][i][0]=sum(dp[N-1][i])%1000000003
    dp[N][i][1]=(dp[N-1][i-1][0])%1000000003
print(sum(dp[N][K]))