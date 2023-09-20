n,m=map(int,input().split())
N=set()
s=0
for i in range(n):
    N.add(input())
for i in range(m):
    if input() in N:
        s+=1
print(s)

from collections import defaultdict
import heapq
def get_lens(a,b):
    return E*(abs(a[0]-b[0])**2+abs(a[1]-b[1])**2)
T=int(input())
for case in range(1,T+1):
    N=int(input())
    land_x=list(map(int,input().split()))
    land_y=list(map(int,input().split()))
    E=float(input())
    graph=defaultdict(list)
    for i in range(N):
        for j in range(i+1,N):
            a=(land_x[i],land_y[i])
            b=(land_x[j],land_y[j])
            graph[a].append((get_lens(a,b),a,b))
            graph[b].append((get_lens(a,b),b,a))
    res=0
    visit={}
    start=(land_x[0],land_y[0])
    visit[start]=1
    cand=graph[start]
    heapq.heapify(cand)
    mst=[]
    while cand:
        weight,u,v=heapq.heappop(cand)
        if v not in visit:
            visit[v]=1
            mst.append((u,v))
            res+=weight
            for edge in graph[v]:
                if edge[2] not in visit:
                    heapq.heappush(cand,edge)

    print(f'#{case}',round(res))