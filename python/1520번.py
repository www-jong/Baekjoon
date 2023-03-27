import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(x,y):
    if dp[x][y]!=-1:
        return dp[x][y]
    if x==M and y==N:
        return 1
    dp[x][y]=0
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 1<=nx<=M and 1<=ny<=N:
            if li[x][y]>li[nx][ny]:
                dp[x][y]+=dfs(nx,ny)
    return dp[x][y]

M,N=map(int,input().split())
li=[[0]]
dp=[[-1]*(N+1) for i in range(M+1)]
for i in range(M):
    li.append([0]+list(map(int,input().split())))
print(dfs(1,1))

'''
M: 세로, N: 가로
dp[i][j]=  출발점에서 (i,j)까지 도달하는 방법수

'''