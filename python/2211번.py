import sys,heapq
INF=int(1e9)
input=sys.stdin.readline


def dtra(start):
    q=[]
    dis=[[INF,[i]] for i in range(N+1)]
    dis[start]=[0,[start]]
    heapq.heappush(q,(0,start))
    while q:
        dist,now=heapq.heappop(q)
        if dist>dis[now][0]:
            continue
        for i in li[now]:
            cost=dist+i[1]
            if cost<dis[i[0]][0]:
                dis[i[0]]=[cost,dis[now][1]+[i[0]]]
                heapq.heappush(q,(cost,i[0]))
    checks={}
    res=[]
    for i in range(2,N+1):
        nowroot=dis[i][1]
        for j in range(len(nowroot)-1):
            nowcheck=cr(nowroot[j],nowroot[j+1])
            if nowcheck not in checks:
                checks[nowcheck]=1
                checks[cr(nowroot[j+1],nowroot[j])]=1
                if nowcheck not in offroot:
                    res.append(str(nowroot[j+1])+' '+str(nowroot[j]))
                else:
                    res.append(str(nowroot[j])+' '+str(nowroot[j+1]))
    print(len(res))
    for i in res:
        print(i)
def cr(a,b):
    return str(a)+'_'+str(b)
N,M=map(int,input().split())
li=[[] for i in range(N+1)]
offroot={}
for i in range(M):
    A,B,C=map(int,input().split())
    offroot[cr(A,B)]=1
    li[A].append((B,C))
    li[B].append((A,C))

dtra(1)
