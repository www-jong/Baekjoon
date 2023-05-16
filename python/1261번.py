import sys,heapq
INF=int(1e9)
input=sys.stdin.readline
M,N=map(int,input().split())
dx=[1,-1,0,0]
dy=[0,0,-1,1]


def dtra():
    q=[]
    dis=[[INF]*(M+1) for _ in range(N+1)]
    dis[1][1]=0
    heapq.heappush(q,(0,[1,1]))

    while q:
        dist,now=heapq.heappop(q)
        x,y=now[0],now[1]
        if dist>dis[x][y]:
            continue
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 1<=nx<=N and 1<=ny<=M:
                cost=dist+li[nx][ny]
                if cost<dis[nx][ny]:
                    dis[nx][ny]=cost
                    heapq.heappush(q,(cost,[nx,ny]))
    print(dis[N][M])
li=[[0]*(M+1)]
for i in range(N):
    tmp=input().rstrip()
    tmpli=[0]
    for i in tmp:
        tmpli.append(int(i))
    li.append(tmpli)
dtra()