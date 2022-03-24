def get_smallest_node():
    min_value=INF
    index=0
    for i in range(1,V+1):
        if dist[i]<min_value and visited[i]!=1:
            min_value=dist[i]
            index=i
    return index

def dij(start):
    dist[start]=0
    visited[start]=1
    for i in graph[start]:
        dist[i[0]]=i[1]
    for i in range(V-1):
        now=get_smallest_node()
        visited[now]=1
        for j in graph[now]:
            cost=dist[now]+j[1]
            if cost<dist[j[0]]:
                dist[j[0]]=cost

INF=int(1e9)
V,E=map(int,input().split())
start=int(input())
graph=[[] for i in range(V+1)]
visited=[0]*(V+1)
dist=[INF]*(V+1)
for i in range(E):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    
dij(start)
for i in range(1,V+1):
    if dist[i]==INF:
        print("INF")
    else:
        print(dist[i])
    
    