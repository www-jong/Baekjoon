N=int(input())
li=[]
for i in range(N):
    li.append(list(map(int,input().split())))
graph=[]
dp=[[[0,0,0] for i in range(N)] for i in range(N)]
dp[0][1][0]=1
for x in range(N):
    for y in range(1,N):
        if li[x][y]==1:continue
        if 0<=y-1<N:
            dp[x][y][0]+=dp[x][y-1][0]+dp[x][y-1][1]
        if 0<=x-1<N and 0<=y-1<N and li[x-1][y]!=1 and li[x][y-1]!=1:
            dp[x][y][1]+=dp[x-1][y-1][0]+dp[x-1][y-1][1]+dp[x-1][y-1][2]
        if 0<=x-1<N:
            dp[x][y][2]+=dp[x-1][y][1]+dp[x-1][y][2]
print(sum(dp[N-1][N-1]))