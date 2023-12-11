import sys,heapq
INF=int(1e9)
d=[0,0,1,-1]
input=sys.stdin.readline
N=int(input())
li=[list(map(int,input().split())) for _ in range(N)]

distance=[[INF]*N for _ in range(N)]
q=[]
heapq.heappush(q,(0,0,0))
distance[0][0]=0
while q:
    dist,x,y=heapq.heappop(q)
    if distance[x][y]<dist:
        continue
    for i in range(4):
        dx=x+d[i]
        dy=y+d[3-i]
        if 0<=dx<N and 0<=dy<N:
            cost=max(dist,abs(li[x][y]-li[dx][dy]))
            if cost<distance[dx][dy]:
                distance[dx][dy]=cost
                heapq.heappush(q,(cost,dx,dy))

print(distance[N-1][N-1])