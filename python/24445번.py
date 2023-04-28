from collections import deque
import sys
input=sys.stdin.readline

N,M,R=map(int,input().split())
graph=[[] for i in range(N+1)]
visit=[0]*(N+1)
for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1,N+1):
    graph[i].sort(reverse=True)

q=deque()
q.append(R)
count=1
visit[R]=count
while q:
    x=q.popleft()
    for i in graph[x]:
        if not visit[i]:
            count+=1
            visit[i]=count
            q.append(i)
for i in range(1,N+1):
    print(visit[i])