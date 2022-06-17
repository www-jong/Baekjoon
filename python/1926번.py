from collections import deque
dx=[0,0,1,-1]
dy=[1,-1,0,0]
n,m=map(int,input().split())
graph=[[0]*(m+1)]
for i in range(n):
    graph.append([0]+list(map(int,input().split())))
max=0
visit=[[0]*(m+1) for i in range(n+1)]
def bfs(visit,node):
    q=deque()
    q.append((node))
    visit[node[0]][node[1]]=1
    count=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 1<=nx<=n and 1<=ny<=m and visit[nx][ny]==0 and graph[nx][ny]==1:
                visit[nx][ny]=1
                q.append((nx,ny))
                count+=1
    return count
com=0
for i in range(1,n+1):
    for j in range(1,m+1):
        if graph[i][j]==0:
            continue
        if visit[i][j]==0:
            s=bfs(visit,(i,j))
            com+=1
            if s>max:
                max=s
print(com)
print(max)       