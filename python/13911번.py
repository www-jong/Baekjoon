import sys,heapq
INF=int(1e12)
input=sys.stdin.readline

def dtra(start,li):
    q=[]
    dis=[INF]*(V+1)
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
    return dis

V,E=map(int,input().split())
mli=[[] for i in range(V+1)]
sli=[[] for i in range(V+1)]
for i in range(E):
    u,v,w=map(int,input().split())
    mli[u].append((v,w))
    sli[u].append((v,w))
    mli[v].append((u,w))
    sli[v].append((u,w))

M,x=map(int,input().split())
for i in list(map(int,input().split())):
    mli[0].append((i,0))
    mli[i].append((0,0))
S,y=map(int,input().split())
for i in list(map(int,input().split())):
    sli[0].append((i,0))
    sli[i].append((0,0))
res=INF

mdis=dtra(0,mli)
sdis=dtra(0,sli)
for i in range(1,V+1):
    mlen=mdis[i] if mdis[i]!=0 else INF
    slen=sdis[i] if sdis[i]!=0 else INF
    if mlen<=x and slen<=y:
        res=min(res,mlen+slen)
print(res)
print(mdis)
print(sdis)