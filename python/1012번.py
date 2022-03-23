import sys
from collections import deque

dx,dy=[-1,1,0,0],[0,0,-1,1]
T=int(input())
for i in range(T):
    M,N,K=map(int,input().split())
    visit=[[0]*(M) for _ in range(N)]
    graph=[[0]*(M) for _ in range(N)]
    for i in range(K):
        b_x,b_y=map(int,sys.stdin.readline().split())
        graph[b_y][b_x]=1
    home=0
    for aa in range(N):
        for bb in range(M):
            q=deque()
            count=0
            if graph[aa][bb]==1 and visit[aa][bb]==0:
                visit[aa][bb]=1
                q.append((aa,bb))
                count=1
            else:continue

            while q:
                x,y=q.popleft()
                if count==2501:
                    break
                for i in range(4):
                    nx=x+dx[i]
                    ny=y+dy[i]
                    if 0<=nx<N and 0<=ny<M:
                        if visit[nx][ny]==0 and graph[nx][ny]==1:
                            visit[nx][ny]=visit[x][y]
                            q.append((nx,ny))
                            count+=1
            if count!=0:home+=1
            

    print(home)