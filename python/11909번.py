import sys
input=sys.stdin.readline
INF=(1e9)
N=int(input())
li=[[0]*(N+1)]
for i in range(N):
    li.append([0]+list(map(int,input().split())))
dp=[[0]*(N+1) for i in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        if i==1 and j==1:
            continue
        tmp1=INF
        tmp2=INF
        if i!=1:
            tmp1=dp[i-1][j]+(li[i][j]-li[i-1][j]+1 if li[i][j]>=li[i-1][j] else 0)
        if j!=1:
            tmp2=dp[i][j-1]+(li[i][j]-li[i][j-1]+1 if li[i][j]>=li[i][j-1] else 0)
        dp[i][j]=min(tmp1,tmp2)
print(dp[N][N])