import sys,heapq
INF=int(1e9)
input=sys.stdin.readline
n,m,r=map(int,input().split())
items=[0]+list(map(int,input().split()))
li=[[] for i in range(1+n)]
for i in range(r):
    a,b,c=map(int,input().split())
    li[a].append((b,c))
    li[b].append((a,c))
res=-1
def dtra(start):
    global res
    q=[]
    dis=[INF]*(n+1)
    dis[start]=0
    heapq.heappush(q,(0,start))
    while q:
        dist,now=heapq.heappop(q)
        if dist>dis[now]:
            continue
        for i in li[now]:
            cost=dist+i[1]
            if cost<dis[i[0]]:
                dis[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    temp=0
    for i in range(1,n+1):
        if dis[i]<=m:
            temp+=items[i]
    res=max(res,temp)

for i in range(1,n+1):
    dtra(i)
print(res)
