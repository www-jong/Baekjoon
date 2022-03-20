import sys
from collections import deque
dx,dy=[-1,1,0,0],[0,0,-1,1]
n,m=map(int,input().split())
visit=[[0]*(m+1) for i in range(n+1)]
graph=[[] for _ in range(n+1)]
for i in range(1,n+1):
    graph[i]=[0]+list(map(int,input()))
q=deque()
q.append((1,1))
visit[1][1]=1
while q:
    x,y=q.popleft()
    if x==n and y==m:
        print(visit[x][y])
        break
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 1<=nx<=n and 1<=ny<=m:
            if visit[nx][ny]==0 and graph[nx][ny]==1:
                visit[nx][ny]=visit[x][y]+1
                q.append((nx,ny))