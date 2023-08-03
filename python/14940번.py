from collections import deque
import sys
input=sys.stdin.readline
dx=[0,0,1,-1]
dy=[1,-1,0,0]
N,M=map(int,input().split())
li,visit=[],[[-1]*(M) for _ in range(N)]
tar=[-1,-1]
for i in range(N):
    tmp=list(map(int,input().split()))
    for j in range(M):
        if tmp[j]==2:
            tar=[i,j]
        elif tmp[j]==0:
            visit[i][j]=0
    li.append(tmp)

q=deque()
q.append((tar[0],tar[1]))
visit[tar[0]][tar[1]]=0
while q:
    x,y=q.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if li[nx][ny]!=0 and visit[nx][ny]==-1:
                visit[nx][ny]=visit[x][y]+1
                q.append((nx,ny))

for i in visit:
    print(*i)