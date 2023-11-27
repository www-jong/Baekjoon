import heapq,sys
input=sys.stdin.readline
N,M,K=map(int,input().split())
graph=[[] for _ in range(N+1)]
INF=int(1e11)
for i in range(M):
    U,V,C=map(int,input().split())
    graph[V].append((U,C))
station=list(map(int,input().split()))
def dstra():
    global res
    q=[]
    for i in station:
        heapq.heappush(q,(0,i))
        distance[i]=0

    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

res=[0,-1]
distance=[INF]*(N+1)
dstra()
for i in range(1,N+1):
    if distance[i]>res[1] and distance[i]!=INF:
        res=[i,distance[i]]
print(res[0])
print(res[1])