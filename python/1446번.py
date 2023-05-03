import heapq,sys
input=sys.stdin.readline
N,D=map(int,input().split())
INF=int(1e9)

def dtra(start):
    q=[]
    dis=[INF]*(10001)
    dis[start]=0
    heapq.heappush(q,(0,start))
    while q:
        dist,now=heapq.heappop(q)
        if dis[now]<dist:
            continue
        for i in li[now]:
            cost=dist+i[1]
            if cost<dis[i[0]]:
                dis[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    return dis

li=[[] for i in range(10001)]
for i in range(D+1):
    li[i].append((i+1,1))
for i in range(N):
    a,b,c=map(int,input().split())
    if b-a>c:
        li[a].append((b,c))
res=dtra(0)
print(res[D])