from collections import deque
import sys
# 정점의 개수, 간선의 개수
n,m=map(int,input().split())
graph=[[0] for i in range(n+1)]
visited=[0]*(n+1)
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n+1):
    graph[i].sort()
count=0

for i in range(1,n+1):        
    if visited[i]==0:
        q=deque()
        q.append(i)
        visited[i]=1
    else:continue
    while q:
        v=q.popleft()
        for j in graph[v]:
            if j==0:continue
            if visited[j]==0:
                q.append(j)
                visited[j]=1
              
    count+=1
print(count)