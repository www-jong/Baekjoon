import sys,heapq
INF=int(1e9)
input=sys.stdin.readline


def dtra(start,end):
    q=[]
    dis=[[INF,[i]] for i in range(n+1)]
    dis[start]=[0,[start]]
    heapq.heappush(q,(0,start))
    while q:
        dist,now=heapq.heappop(q)
        if dist>dis[now][0]:
            continue
        for i in li[now]:
            cost=dist+i[1]
            if cost<dis[i[0]][0]:
                mindex[now].append(i[0])
                dis[i[0]]=[cost,dis[now][1]+[i[0]]]
                heapq.heappush(q,(cost,i[0]))
    print(dis[end][0])
    print(len(dis[end][1]))
    print(*dis[end][1])
n=int(input())
m=int(input())
mindex=[[] for i in range(n+1)]
li=[[] for _ in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())
    li[a].append((b,c))
start,end=map(int,input().split())

dtra(start,end)