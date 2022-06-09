# 시간초과
from collections import deque
import sys
sys.setrecursionlimit(10**7)
n,m=map(int,input().split())
graph=[[0]*(m+1)]
for i in range(n):
    li=[]
    for j in "0"+input():
        li.append(int(j))
    graph.append(li)
dx,dy=[-1,1,0,0],[0,0,-1,1]
visit=[[0]*(m+1) for i in range(n+1)]
movelist=[]
def bfs(graph,visit,check,node,q):
    global movelist
    if check==0:
        q.append((node[0],node[1]))
        visit[node[0]][node[1]]=1
    while q:
        x,y=q.popleft()
        wells=[]
        if x==n and y==m:
            movelist.append(visit[x][y])
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 1<=nx<=n and 1<=ny<=m:
                if check==0 and graph[nx][ny]==1:
                    wells.append((nx,ny))
                    check=1
                elif visit[nx][ny]==0 and graph[nx][ny]==0:
                    visit[nx][ny]=visit[x][y]+1
                    q.append((nx,ny))
        if check==1:
            for sx,sy in wells:
                q.append((sx,sy))
                visit[sx][sy]=visit[x][y]+1
                graph[sx][sy]=0
                bfs(graph,visit,1,(sx,sy),q)
                if q:
                    q.pop()
                graph[sx][sy]=1
                visit[sx][sy]=0
            check=0
q=deque()
bfs(graph,visit,0,(1,1),q)
if len(movelist)<1:
    print(-1)
else:
    print(min(movelist))

