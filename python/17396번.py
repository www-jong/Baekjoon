import sys,heapq
INF=int(1e15)
input=sys.stdin.readline
N,M=map(int,input().split())



def dtra(start):
    q=[]
    dis=[INF]*(N+1)
    dis[start]=0
    heapq.heappush(q,(0,start))
    while q:
        dist,now=heapq.heappop(q)
        if dis[now]<dist:
            continue
        for i in li[now]:
            if check[i[0]]==1:
                continue
            cost=dist+i[1]
            if cost<dis[i[0]]:
                dis[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    return dis

check=list(map(int,input().split()))
check[N-1]=0
li=[[] for i in range(N+1)]
for i in range(M):
    a,b,c=map(int,input().split())
    li[a].append((b,c))
    li[b].append((a,c))

rdis=dtra(0)
print(rdis[N-1] if rdis[N-1]!=INF else -1)