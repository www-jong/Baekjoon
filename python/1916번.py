import heapq
import sys
INF=int(1e9)
n=int(input())
m=int(input())
f_graph={}
graph=[[] for i in range(n+1)]
dis=[INF]*(n+1)

for i in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    if (a,b) not in f_graph:
        f_graph[(a,b)]=c
    else:
        if f_graph[(a,b)]>c:
            f_graph[(a,b)]=c
for key,val in f_graph.items():
    graph[key[0]].append((key[1],val))
start,end=map(int,input().split())
q=[]
heapq.heappush(q,(0,start))
dis[start]=0
while q:
    d,now=heapq.heappop(q)
    if dis[now]<d:
        continue
    for i in graph[now]:
        cost=d+i[1]
        if cost<dis[i[0]]:
            dis[i[0]]=cost
            heapq.heappush(q,(cost,i[0]))
print(dis[end])