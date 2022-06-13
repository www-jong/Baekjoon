from collections import deque

def bfs(node):
    q=deque()
    q.append(node)
    while q:
        node=q.popleft()
        for n in graph[node]:
            if visit[n]==0:
                visit[n]=visit[node]+1
                q.append(n)
n=int(input())
a,b=map(int,input().split())
m=int(input())
graph=[[] for i in range(n+1)]

for i in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
visit=[0]*(n+1)
bfs(a)
print(visit[b] if visit[b]>0 else -1)