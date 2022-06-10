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
visit=[[[0,0] for i in range(m+1)] for i in range(n+1)]
ans=100000000
def bfs(graph,visit,node,q):
    global ans
    q.append((node[0],node[1],node[2]))
    visit[node[0]][node[1]][node[2]]=1
    while q:
        x,y,st=q.popleft()
        if x==n and y==m:
            if visit[x][y][st]<ans:
                ans=visit[x][y][st]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 1<=nx<=n and 1<=ny<=m:
                if visit[nx][ny][st]==0 and graph[nx][ny]==0:
                    visit[nx][ny][st]=visit[x][y][st]+1
                    q.append((nx,ny,st))
                if graph[nx][ny]==1 and st==0:
                    visit[nx][ny][1]=visit[x][y][st]+1
                    q.append((nx,ny,1))
q=deque()
bfs(graph,visit,(1,1,0),q)
if ans==100000000:
    print(-1)
else:
    print(ans)

