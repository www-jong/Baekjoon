import heapq,sys
input=sys.stdin.readline
N,M=map(int,input().split())
road=[[] for _ in range(N+1)]
INF=int(1e10)
def dstra(ban):
    q=[]
    distance=[INF]*(N+1)
    heapq.heappush(q,(0,1))
    distance[1]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for idx,b,c in road[now]:
            if ban==idx:
                continue
            cost=dist+c
            if cost<distance[b]:
                distance[b]=cost
                heapq.heappush(q,(cost,b))
    return distance[N]
for idx in range(1,M+1):
    a,b,t=map(int,input().split())
    road[a].append((idx,b,t))
    road[b].append((idx,a,t))
q=[]
distance=[INF]*(N+1)
rg=[]
heapq.heappush(q,(0,1,[]))
distance[1]=0
while q:
    dist,now,root=heapq.heappop(q)
    if distance[now]<dist:
        continue
    for idx,b,c in road[now]:
        cost=dist+c
        if cost<distance[b]:
            distance[b]=cost
            heapq.heappush(q,(cost,b,root+[idx]))
            if b==N:
                rg=root+[idx]
rg=set(rg)
v=distance[N]
res=0
for i in list(rg):
    #print(i,dstra(i),v)
    g=dstra(i)
    if g==INF:
        res=-1
        break
    res=max(res,g-v)
print(res)
