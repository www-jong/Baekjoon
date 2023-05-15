import heapq,sys
INF=int(1e9)
input=sys.stdin.readline
dx=[0,0,-1,1]
dy=[1,-1,0,0]
def dtra(N):
    q=[]
    dis=[[INF]*(N) for _ in range(N)]
    dis[0][0]=li[0][0]
    heapq.heappush(q,(li[0][0],[0,0]))
    while q:
        dist,now=heapq.heappop(q)
        if dis[now[0]][now[1]]<dist:
            continue
        for i in range(4):
            nx=now[0]+dx[i]
            ny=now[1]+dy[i]
            if 0<=nx<=N-1 and 0<=ny<=N-1:
                cost=dist+li[nx][ny]
                if cost<dis[nx][ny]:
                    dis[nx][ny]=cost
                    heapq.heappush(q,(cost,[nx,ny]))
    print(f'Problem {co}: {dis[N-1][N-1]}')
co=0
while True:
    N=int(input())
    co+=1
    if N==0:
        break
    li=[]
    for i in range(N):
        li.append(list(map(int,input().split())))
    dtra(N)
    

