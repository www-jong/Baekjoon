import heapq
INF=float(1e9)
def tur(x):
    tmp=[]
    for i in x:
        tmp.append(ord(i)-(71 if i.islower() else 65))
    return tmp
def dstra(st,type):
    distance=[[INF]*(M) for _ in range(N)]
    q=[]
    heapq.heappush(q,(0,st[0],st[1]))
    distance[st[0]][st[1]]=0
    while q:
        dist,x,y=heapq.heappop(q)
        if dist>distance[x][y]:
            continue
        for i in range(4):
            nx,ny=x+d[i],y+d[3-i]
            if 0<=nx<N and 0<=ny<M and abs(li[x][y]-li[nx][ny])<=T:
                if type==0:
                    cost = dist + (1 if li[x][y] <= li[nx][ny] else (li[x][y] - li[nx][ny]) ** 2)
                else:
                    cost = dist + (1 if li[x][y] >= li[nx][ny] else (li[x][y] - li[nx][ny]) ** 2)
                if distance[nx][ny]>cost:
                    distance[nx][ny]=cost
                    heapq.heappush(q,(cost,nx,ny))
    return distance
N,M,T,D=map(int,input().split())
li=[tur(input()) for _ in range(N)]
d=[0,0,1,-1]
a=dstra((0,0),1)
b=dstra((0,0),0)

res=[]
r=-1
for i in range(N):
    for j in range(M):
        if li[i][j]>r and a[i][j]+b[i][j]<=D:
            r=li[i][j]
        res.append([li[i][j],a[i][j]+b[i][j]])
res.sort()
print(r)