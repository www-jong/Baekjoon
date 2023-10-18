import heapq
import sys
input=sys.stdin.readline
INF=int(1e10)
N,K=map(int,input().split())
def find(a):
    if a==nodes[a]:
        return nodes[a]
    nodes[a]=find(nodes[a])
    return nodes[a]

def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        if a<b:
            nodes[b]=a
        else:
            nodes[a]=b

def dstra(st):
    distance=[INF]*N
    q=[]
    heapq.heappush(q,(0,st))
    distance[st]=0
    while q:
        dist,now=heapq.heappop(q)
        if dist>distance[now]:
            continue
        for i in g[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    tmp=0
    for i in range(N):
        if distance[i]!=INF and distance[i]>tmp:
            tmp=distance[i]
    return tmp

nodes=[i for i in range(N+1)]
graph1=[]

for _ in range(K):
    a,b,c=map(int,input().split())
    graph1.append((a,b,c))
graph1.sort(key=lambda x:x[2])

r1,r2=0,0
g=[[] for _ in range(N)]
for a,b,c in graph1:
    if find(a)!=find(b):
        r1+=c
        union(a,b)
        g[a].append((b,c))
        g[b].append((a,c))
for st in range(N):
    r2=max(r2,dstra(st))
print(r1)
print(r2)