from collections import deque
def bfs(node):
    global n
    visit=[0]*(n+1)
    q=deque()
    q.append(node)
    while q:
        node2=q.popleft()
        for i in graph[node2]:
            if visit[i]==0:
                visit[i]=visit[node2]+1
                q.append(i)
    return sum(visit)
n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
bacon=1000000000
ans=0
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1,n+1):
    d=bfs(i)
    if bacon>d:
        bacon=d
        ans=i
print(ans)
