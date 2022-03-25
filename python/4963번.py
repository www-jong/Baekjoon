from collections import deque
dx=[1,-1,0,0,1,1,-1,-1]
dy=[0,0,-1,1,1,-1,1,-1]

while True:
    count=0
    w,h=map(int,input().split())
    if w==0 and h==0:break
    graph=[[0]]
    for i in range(h):
        graph.append([0]+list(map(int,input().split())))
    visited=[[0]*(w+1) for i in range(h+1)]
    q=deque()
    for i in range(1,h+1):
        for j in range(1,w+1):
            if graph[i][j]==1 and visited[i][j]==0:
                q.append((i,j))
            else:continue
            visited[i][j]=1
            while q:
                x,y=q.popleft()
                for s in range(8):
                    nx=x+dx[s]
                    ny=y+dy[s]
                    if 0<nx<=h and 0<ny<=w:
                        if graph[nx][ny]==1 and visited[nx][ny]==0:
                            q.append((nx,ny))
                            visited[nx][ny]=1
            count+=1
    print(count)