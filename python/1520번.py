from collections import deque
import sys
input=sys.stdin.readline
M,N=map(int,input().split())
li=[[0]]
dp=[[0]*(N+1) for i in range(M+1)]
for i in range(M):
    li.append([0]+list(map(int,input().split())))
dx=[0,0,1,-1]
dy=[1,-1,0,0]
dp[1][1]=1
q=deque()
q.append((1,1))
while q:
    x,y=q.popleft()
    now=dp[x][y]
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 1<=nx<=M and 1<=ny<=N and li[nx][ny]<li[x][y]:
            dp[nx][ny]+=dp[x][y]
            q.append((nx,ny))
print(dp[M][N])

print('---')
for i in dp:
    print(i)

'''
dp[i][j]=  출발점에서 (i,j)까지 도달하는 방법수

'''