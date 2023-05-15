import heapq,sys
INF=int(1e9)
input=sys.stdin.readline
dx=[0,0,-1,1]
dy=[1,-1,0,0]

def dtra(N):
    q=[]
    dis=[[INF]*(N) for _ in range(N)]
    dis[0][0]=0
    heapq.heappush(q,(0,[0,0]))
    while q:
        dist,now=heapq.heappop(q)
        x,y=now[0],now[1]
        if dis[x][y]<dist:
            continue
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<=N-1 and 0<=ny<=N-1:
                cost=dist+li[nx][ny]
                if cost<dis[nx][ny]:
                    dis[nx][ny]=cost
                    heapq.heappush(q,(cost,[nx,ny]))
    print(dis[N-1][N-1])
n=int(input())
li=[]
for i in range(n):
    tmp=input()
    tmpli=[]
    for i in tmp:
        tmpli.append(int(0) if i=='1' else int(1))
    li.append(tmpli)
dtra(n)