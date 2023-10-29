import sys,heapq
d=[[[0,1],[0,-1],[1,0],[-1,0]],[[1,0],[-1,0]],[[0,1],[0,-1]]]
input=sys.stdin.readline
def f(x):
    return int(x)-1
N,M=map(int,input().split())
sx,sy,ex,ey=map(f,input().split())
li=[list(map(int,input().split())) for _ in range(N)]
INF=int(1e10)
distance=[[[INF]*M for _ in range(N)] for _ in range(3)]
distance[1][sx][sy]=0
q=[]
heapq.heappush(q,(0,1,(sx,sy)))
while q:
    dist,turn,now=heapq.heappop(q)
    if dist>distance[turn][now[0]][now[1]]:
        continue
    for nx,ny in d[turn]:
        dx,dy=now[0]+nx,now[1]+ny
        next_turn=(turn+1)%3
        if 0<=dx<N and 0<=dy<M and dist+li[dx][dy]<distance[next_turn][dx][dy]:
            if li[dx][dy]==-1:
                continue
            cost=dist+li[dx][dy]
            distance[next_turn][dx][dy]=cost
            heapq.heappush(q,(cost,next_turn,(dx,dy)))
r=INF
for i in range(3):
    r=min(r,distance[i][ex][ey])
print(-1 if r==INF else r)