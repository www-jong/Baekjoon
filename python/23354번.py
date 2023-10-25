import sys,heapq
input=sys.stdin.readline
INF=int(1e9)
d=[0,0,1,-1]
N=int(input())
st=[0,0]
tar=[]
li=[]
res=10**9
for i in range(N):
    tmp=list(map(int,input().split()))
    for j in range(N):
        if tmp[j]==-1:
            st=[i,j]
            tmp[j]=0
        elif tmp[j]==0:
            tar.append((i,j))
    li.append(tmp)
def func(c,l):
    global res
    if len(l)==len(tar):
        res=min(res,c+cost[l[-1]][st[0]][st[1]])
        return
    if c>res:
        return
    for i in range(len(tar)):
        if i not in l:
            func(c+cost[l[-1]][tar[i][0]][tar[i][1]],l+[i])

def dstra(st):
    distance=[[INF]*N for _ in range(N)]
    q=[]
    heapq.heappush(q,(0,st))
    distance[st[0]][st[1]]=0
    while q:
        dist,now=heapq.heappop(q)
        if dist>distance[now[0]][now[1]]:
            continue
        for i in range(4):
            nx,ny=now[0]+d[i],now[1]+d[3-i]
            if 0<=nx<N and 0<=ny<N and dist+li[nx][ny]<distance[nx][ny]:
                distance[nx][ny]=dist+li[nx][ny]
                heapq.heappush(q,(dist+li[nx][ny],(nx,ny)))
    return distance
st_cost=dstra(st)
cost=[dstra(i) for i in tar]

for i in range(len(tar)):
    dx,dy=tar[i]
    func(st_cost[dx][dy],[i])
print(0 if res==INF else res)