from collections import deque
import sys
def bfs(visit,start):
    q=deque()
    count=0
    q.append(start)
    visit[start]=1
    while q:
        com=q.popleft()
        for i in graph[com]:
            if visit[i]==0:
                q.append(i)
                visit[i]=1
                count+=1
    return count
n,m=map(int,sys.stdin.readline().split())
max=-10000
graph=[[] for i in range(n+1)]
visit=[0]*(n+1)
ans=[]
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[b].append(a)
for i in range(1,n+1):
    visit2=visit.copy()
    g=bfs(visit2,i)
    if g>max:
        ans.clear()
        ans.append(i)
        max=g
    elif g==max:
        ans.append(i)
print(*ans)