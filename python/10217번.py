import sys,heapq
INF=int(1e9)
input=sys.stdin.readline

for i in range(int(input())):
    N,M,K=map(int,input().split())
    li=[[] for i in range(N+1)]
    for _ in range(K):
        u,v,c,d=map(int,input().split())
        li[u].append((v,c,d))
        li[v].append((u,c,d))
    dp=[[0]*(M+1) for i in range(N+1)]
    
    q=[]
    dis=[INF]*(M+1)
    start=1
    heapq.heappush(q,(0,start))
    while q:
        dist,now=heapq.heappop(q)
        if dist>dis[now]:
            continue
        for i in li[now]:
            cost=dist+i[1]
            if cost<dis[i[0]]:
                

'''
c=비용
d=소요시간

m이하의 비용으로 최소의 d
dis[i]=[[a,b],[c,d],[e,f],......] -> [a,b] -> 
'''