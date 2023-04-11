# 단순하게 벽마다 bfs를 진행하는 방법.
# 시간초과
import sys
from collections import deque
input=sys.stdin.readline
N,M=map(int,input().split())
li=[[0]]
res=[[0]]
walls=[]
dx=[0,0,-1,1]
dy=[1,-1,0,0]

for i in range(1,N+1):
    tmp='0'+input()
    tmpli=[]
    for j in range(M+1):
        tmpli.append(int(tmp[j]))
        if tmp[j]=='1':
            walls.append([i,j])
    li.append(tmpli)
    res.append(tmpli)

for wx,wy in walls:
    q=deque()
    q.append((wx,wy))
    count=1
    visit=[[0]*(M+1) for i in range(N+1)]
    visit[wx][wy]=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 1<=nx<=N and 1<=ny<=M:
                if visit[nx][ny]==0 and li[nx][ny]==0:
                    count+=1
                    q.append((nx,ny))
                    visit[nx][ny]=1
    res[wx][wy]=count%10
for i in res:
    print(*i[1:],sep='')