import sys,heapq
INF=int(1e9)
input=sys.stdin.readline
sys.setrecursionlimit(10000000)

N,E=map(int,input().split())
nodes=[i for i in range(N+1)]


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
            cost=dist+i[1]
            if cost<dis[i[0]]:
                dis[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    return dis
li=[[] for i in range(N+1)]
for i in range(E):
    a,b,c=map(int,input().split())
    li[a].append((b,c))
    li[b].append((a,c))
u,v=map(int,input().split())
s,u1,v1=dtra(1),dtra(u),dtra(v)
print(f's[u]:{s[u]}, s[v]:{s[v]}, u1[v]:{u1[v]}, v1[u]:{v1[u]}, u1[N]:{u1[N]}, v1[N]:{v1[N]}')
res=min(s[u]+u1[v]+v1[N],s[v]+v1[u]+u1[N])
print(res if res<INF else -1)
#print(f's1:{s1}, s2:{s2}, m:{m}, e1:{e1}, e2:{e2}')