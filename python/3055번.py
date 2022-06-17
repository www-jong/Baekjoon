from collections import deque
r,c=map(int,input().split())
graph=[[0]*(c+1)]
start=()
end=()
dx=[0,0,-1,1]
dy=[1,-1,0,0]
wlist=[]
visit=[[0]*(c+1) for i in range(r+1)]
watermap=[[20000]*(c+1) for i in range(r+1)]
for i in range(r):
    s=list(input().replace('.','0').replace('*','1').replace('X','3'))
    li=[0]
    for j in range(len(s)):
        if s[j]=='S':
            start=(i+1,j+1)
            s[j]='0'
        elif s[j]=='D':
            end=(i+1,j+1)
            watermap[i+1][j+1]=20001
            s[j]='-2'
        elif s[j]=='1':
            watermap[i+1][j+1]=1
            wlist.append((i+1,j+1))
        li.append(int(s[j]))
    graph.append(li)
def water(wlist):
    q=deque(wlist)
    newwlist=[]
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 1<=nx<=r and 1<=ny<=c:
                if graph[nx][ny]==0 and watermap[nx][ny]==20000:
                    watermap[nx][ny]=watermap[x][y]+1
                    newwlist.append((nx,ny))
    return newwlist

for i in range(20):
    wlist=water(wlist)
def bfs(visit,node):
    q=deque()
    q.append(node)
    visit[node[0]][node[1]]=1
    while q:
        x,y=q.popleft()
        if x==end[0] and y==end[1]:
            return visit[x][y]
            break
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 1<=nx<=r and 1<=ny<=c:
                if graph[nx][ny]==0 or graph[nx][ny]==-2:
                    if visit[nx][ny]==0 and watermap[nx][ny]>(visit[x][y]+1):
                        visit[nx][ny]=visit[x][y]+1
                        q.append((nx,ny))
    
g=bfs(visit,start)
if g:
    print(g-1)
else:
    print('KAKTUS')
'''
print('water')
for i in range(1,r+1):
    print(watermap[i])
print('graph')
for i in range(1,r+1):
    print(graph[i])
print('visit')
for i in range(1,r+1):
    print(visit[i])
print('start :',start)
print('end :',end)
'''