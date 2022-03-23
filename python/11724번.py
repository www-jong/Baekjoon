from collections import deque

n,m=map(int,input().split())
graph=[[0]*(n+1) for i in range(n+1)]
visited=[0]*(n+1)
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n+1):
    graph[i].sort()
count=0

for i in range(1,n+1):        
    if sum(graph[i])==0:
        continue
    else:
        ss=[]
        q=deque()
        q.append(i)
        visited[i]=1
        while q:
            v=q.popleft()
            for j in graph[v]:
                if visited[j]==0:
                    q.append(j)
                    visited[j]=1

        for i in range(n+1):
            if visited[i]==1:
                graph[i]=[0]*(n+1)                
        count+=1

print(count)

