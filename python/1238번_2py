import heapq,sys
input=sys.stdin.readline
inf=int(1e9)

n,m,x=map(int,input().split())
graph=[[] for _ in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def distra(start):
    q=[]
    dis=[inf]*(n+1)
    heapq.heappush(q,(0,start))
    dis[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if dis[now]<dist:
            continue
        for node_index,node_cost in graph[now]:
            cost=dist+node_cost
            if dis[node_index]>cost:
                dis[node_index]=cost
                heapq.heappush(q,(cost,node_index))
    return dis

result=0
for i in range(1,n+1):
    go=distra(i)
    back=distra(x)
    result=max(result,go[x]+back[i])
print(result)