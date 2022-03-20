import sys
from collections import deque
def bfs(g,v,visit):
    #print(g)
    queue=deque()
    queue.append(v)
    visit[v]=True
    while queue:
        s=queue.popleft()
        print(s,end=' ')
        for i in g[s]:
            if not visit[i]:
                queue.append(i)
                visit[i]=True
                
def dfs(g,v,visit):
    visit[v]=True
    print(v,end=' ')
    for i in g[v]:
        if not visit[i]:
            dfs(g,i,visit)

n,m,v=map(int,input().split())
g=[[] for _ in range(n+1)]
visit=[False]*(n+1)
visit2=[False]*(n+1)
for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    g[a].append(b)
    g[b].append(a)
for i in range(n+1):
    g[i].sort()
dfs(g,v,visit2)
print()
bfs(g,v,visit)
