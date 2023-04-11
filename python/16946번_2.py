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
visit=[[[0,0,0] for _ in range(M+1)] for i in range(N+1)]
# [방문체크,주변칸수,덩어리번호]
co=1
for x in range(1,N+1):
    for y in range(1,M+1):
        if li[x][y]==1 or visit[x][y][0]==1:
            continue
        q=deque()
        q.append((x,y))
        visit[x][y][0]=1
        visit[x][y][2]=co
        count=1
        tmp_li=[[x,y]]
        while q:
            sx,sy=q.popleft()
            for i in range(4):
                nx=sx+dx[i]
                ny=sy+dy[i]
                if 1<=nx<=N and 1<=ny<=M:
                    if visit[nx][ny][0]==0 and li[nx][ny]==0:
                        q.append((nx,ny))
                        count+=1
                        visit[nx][ny][0]=1
                        visit[nx][ny][2]=co
                        tmp_li.append([nx,ny])
        for rx,ry in tmp_li:
            visit[rx][ry][1]=count

        co+=1
for x,y in walls:
    tmp={}
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 1<=nx<=N and 1<=ny<=M:
            if visit[nx][ny][2] not in tmp:
                tmp[visit[nx][ny][2]]=1
                res[x][y]+=visit[nx][ny][1]
    res[x][y]%=10

for i in range(1,N+1):
    print(*res[i][1:],sep='')

for i in visit:
    print(i)