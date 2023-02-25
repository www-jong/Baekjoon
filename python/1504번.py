import sys
import heapq
input=sys.stdin.readline
INF=int(1e9)
N,E=map(int,input().split())
li=[[] for i in range(N+1)]
dis=[INF]*(N+1)
visit=[0]*(N+1)

for i in range(E):
    a,b,c=map(int,input().split())
    li[a].append((b,c))
    li[b].append((b,c))
v1,v2=map(int,input().split())

def func(st):
    q=[]
    heapq.heappush(q,(0,st))
    dis[st]=0
    while q:
        dist,now=heapq.heappop()
        if dis[now]<dist:
            continue
        for i in li[now]:
            cost=dist+i[1]
            if cost<dis[i[0]]:
                dis[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
func(1)
for i in range(1,N+1):
    print(dis[i])