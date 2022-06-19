# bfs
import sys
from collections import deque
n,m,x=map(int,sys.stdin.readline().split())
graph=[[] for i in range(1+n)]
for i in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    graph[a].append((b,c))

def bfs(node,end,mode):
    visit=[-1]*(n+1)
    q=deque()
    q.append((node))
    visit[node]=0
    min=10**9
    while q:
        now=q.popleft()
        if now==end:
            if visit[now]<min:
                min=visit[now]
        for i,j in graph[now]:
            if visit[i]==-1:
                visit[i]=visit[now]+j
                q.append((i))
            elif visit[i]>visit[now]+j:
                visit[i]=visit[now]+j
                q.append((i))
    if mode==0:
        return min+bfs(end,node,1)
    else:
        return min
max=-1
ans=-1
for i in range(1,n+1):
    val=bfs(i,x,0)
    if val:
        if val>max:
            max=val
            ans=i
print(max)