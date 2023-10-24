import sys,heapq
input=sys.stdin.readline
N,M=map(int,input().split())
INF=int(1e9)
graph=[[]for _ in range(N+1)]
def go(x):
    if x==2:
        return 1
    if dp[x]:
        return dp[x]
    for i in graph[x]:
        if distance[x]>distance[i[0]]:
            dp[x]+=go(i[0])
    return dp[x]

for _ in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

distance=[INF]*(N+1)
q=[]
heapq.heappush(q,(0,2))
distance[2]=0
while q:
    dist,now=heapq.heappop(q)
    if dist>distance[now]:
        continue
    for i in graph[now]:
        cost=dist+i[1]
        if distance[i[0]]>cost:
            distance[i[0]]=cost
            heapq.heappush(q,(cost,i[0]))
print(distance)
dp=[0]*(N+1)
go(1)
print(dp[1])