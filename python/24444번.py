from collections import deque
import sys
input=sys.stdin.readline
n,m,r=map(int,input().split())
graph=[[] for i in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1,n+1):
    graph[i].sort()
q=deque()
q.append(r)
visit=[0]*(n+1)
visit[r]=1
co=2
while q:
    x=q.popleft()
    for i in graph[x]:
        if visit[i]==0:
            visit[i]=co
            co+=1
            q.append(i)
for i in range(1,n+1):
    print(visit[i])
'''
for i in range(1,n+1):
    print(ans[i])
'''