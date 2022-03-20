import sys
from collections import deque

dx,dy=[-1,1,0,0],[0,0,-1,1]
n=int(input())
visit=[[0]*(n+1) for i in range(n+1)]
graph=[[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    graph[i]=[0]+list(map(int,input()))

home=[]
dong=2
for aa in range(1,n+1):
    for bb in range(1,n+1):
        q=deque()
        if graph[aa][bb]==1 and visit[aa][bb]==0:
            visit[aa][bb]=dong
            q.append((aa,bb))
            count=1
        else:continue

        while q:
            x,y=q.popleft()
            if count==625:
                break
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 1<=nx<=n and 1<=ny<=n:
                    if visit[nx][ny]==0 and graph[nx][ny]==1:
                        visit[nx][ny]=visit[x][y]
                        q.append((nx,ny))
                        count+=1
        dong+=1
        home.append(count)
        
home.sort()
print(len(home))
print(*home,sep="\n")