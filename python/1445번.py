import heapq
N,M=map(int,input().split())
INF=int(1e9)
st,end=[0,0],[0,0]
li=[[0]*(M) for _ in range(N)]
distance=[[INF]*(M) for _ in range(N)]
u_distance=[[INF]*(M) for _ in range(N)]
d=[0,0,1,-1]
dirty=[]
for i in range(N):
    tmp=input()
    for j in range(M):
        if tmp[j]=='S':
            st=[i,j]
        if tmp[j]=='F':
            end=[i,j]
        if tmp[j]=='g':
            dirty.append([i,j])
for i,j in dirty:
    li[i][j]=2
for i,j in dirty:
    for k in range(4):
        ni,nj=i+d[k],j+d[3-k]
        if 0<=ni<N and 0<=nj<M and li[ni][nj]==0:
            li[ni][nj]=1
li[st[0]][st[1]]=0
li[end[0]][end[1]]=0

q=[]
heapq.heappush(q,(0,0,st))
distance[st[0]][st[1]]=0
while q:
    dist_1,dist_2,now=heapq.heappop(q)
    if distance[now[0]][now[1]]<dist_1:
        continue

    for i in range(4):
        nx,ny=now[0]+d[i],now[1]+d[3-i]
        cost_1,cost_2=dist_1,dist_2
        c=0
        if 0<=nx<N and 0<=ny<M:
            if li[nx][ny]==2:
                cost_1+=1
                cost_2+=1
            elif li[nx][ny]==1:
                cost_2+=1
            if cost_1<distance[nx][ny]:
                distance[nx][ny]=cost_1
                u_distance[nx][ny]=cost_2
                heapq.heappush(q,(cost_1,cost_2,(nx,ny)))
            elif cost_1==distance[nx][ny] and cost_2<u_distance[nx][ny]:
                u_distance[nx][ny]=cost_2
                heapq.heappush(q,(cost_1,cost_2,(nx,ny)))

print(distance[end[0]][end[1]],u_distance[end[0]][end[1]]-distance[end[0]][end[1]])

