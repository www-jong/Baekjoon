import sys,heapq
INF=int(1e12)
input=sys.stdin.readline

N,M,K=map(int,input().split())

li=[[] for i in range(N+1)]



for i in range(M):
    a,b,c=map(int,input().split())
    li[a].append((b,c))
    li[b].append((a,c))

q=[]
dis=[[INF]*(K+1) for _ in range(N+1)]
dis[1]=[0]*(K+1)
heapq.heappush(q,(0,1,0))
while q:
    dist,now,co=heapq.heappop(q)
    if dist>dis[now][co]:
        continue
    if co+1<=K:
        for i in li[now]:
            if dist<dis[i[0]][co+1]:
                dis[i[0]][co+1]=dist
                heapq.heappush(q,(dist,i[0],co+1))
    
    for i in li[now]:
        cost=dist+i[1]
        if cost<dis[i[0]][co]:
            dis[i[0]][co]=cost
            heapq.heappush(q,(cost,i[0],co))
print(min(dis[N]))