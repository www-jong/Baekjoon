from collections import deque
N,M=map(int,input().split())
maps=[]
keys=[]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
for i in range(N):
    tmp=input()
    tmp_li=[i for i in tmp]
    for j in range(N):
        if tmp_li[j]=='S' or tmp_li[j]=='K':
            keys.append([i,j])
    maps.append(tmp_li)


li=[]
nodes=[i for i in range(len(keys)+1)]
def bfs(sx,sy,ex,ey):
    global maps
    q=deque()
    q.append((sx,sy))
    visit=[[10**9]*(N) for i in range(N)]
    visit[sx][sy]=0
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 1<=nx<=N-2 and 1<=ny<=N-2:
                if maps[nx][ny]!='1' and visit[nx][ny]==10**9:
                    visit[nx][ny]=min(visit[x][y]+1,visit[nx][ny])
                    if nx==ex and ny==ey:
                        return visit[nx][ny]
                    q.append((nx,ny))

def find(a):
    if a==nodes[a]:
        return a
    nodes[a]=find(nodes[a])
    return nodes[a]

def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        if a<b:
            nodes[b]=a
        else:
            nodes[a]=b

res=0
for i in range(len(keys)):
    for j in range(i+1,len(keys)):
        now_val=bfs(keys[i][0],keys[i][1],keys[j][0],keys[j][1])
        if now_val:
            li.append([i,j,now_val])
        else:
            res=-1
            print(res)
            break
    if res==-1:
        break

if res!=-1:
    li.sort(key=lambda x:x[2])
    for x,y,c in li:
        if find(x)!=find(y):
            res+=c
            union(x,y)
    print(res)