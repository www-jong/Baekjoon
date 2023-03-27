from collections import deque
dx=[1,-1,0,0]
dy=[0,0,1,-1]

N,M,K=map(int,input().split())
li=[[0]*(M+1) for i in range(N+1)]
visit=[[0]*(M+1) for i in range(N+1)]
res=-1
for i in range(K):
    x,y=map(int,input().split())
    if 1<=x<=N and 1<=y<=M:
        li[x][y]=1

for a in range(1,N+1):
    for b in range(1,M+1):
        q=deque()
        tmp=0
        if li[a][b]==1 and visit[a][b]==0:
            q.append((a,b))
        while q:
            x,y=q.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 1<=nx<=N and 1<=ny<=M:
                    if not visit[nx][ny] and li[nx][ny]:
                        visit[nx][ny]=1
                        q.append((nx,ny))
                        tmp+=1
        res=max(tmp,res)
print(res)
