from collections import deque
def bfs(graph,st,visited):
    q=deque()
    count=-1
    q.append(st)
    visited[st]=1
    while q:
        v=q.popleft()
        count+=1
        for i in graph[v]:
            if visited[i]==0:
                q.append(i)
                visited[i]=1
    print(count)
    
    
n=int(input())
visited=[0]*(n+1)
graph=[[] for i in range(n+1)]
s=int(input())
for i in range(s):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1,n+1):
    graph[i].sort()
bfs(graph,1,visited)