import sys,heapq
INF=int(1e12)
input=sys.stdin.readline

N,M=map(int,input().split())
li=[[] for i in range(N+1)]

for i in range(M):
    a,b,c=map(int,input().split())
    c=c*2
    li[a].append((b,c))
    li[b].append((a,c))

q=[]
fdis=[INF]*(N+1)
fdis[1]=0
heapq.heappush(q,(0,1))
while q:
    dist,now=heapq.heappop(q)
    if dist>fdis[now]:
        continue
    for i in li[now]:
        cost=dist+i[1]
        if cost<fdis[i[0]]:
            fdis[i[0]]=cost
            heapq.heappush(q,(cost,i[0]))

q=[]
wdis=[[INF]*(2) for i in range(N+1)]
wdis[1]=[INF,INF]
heapq.heappush(q,(0,1,0))
while q:
    dist,now,co=heapq.heappop(q)
    if co==0:
        if dist>wdis[now][1]:
            continue
        for i in li[now]:
            cost=dist+i[1]//2
            if cost<wdis[i[0]][0]:
                wdis[i[0]][0]=cost
                heapq.heappush(q,(cost,i[0],1))
    else:
        if dist>wdis[now][0]:
            continue
        for i in li[now]:
            cost=dist+i[1]*2
            if cost<wdis[i[0]][1]:
                wdis[i[0]][1]=cost
                heapq.heappush(q,(cost,i[0],0))

res=0
for i in range(2,N+1):
    if fdis[i]<min(wdis[i]):
        res+=1
print(res)
print(fdis)
print(wdis)