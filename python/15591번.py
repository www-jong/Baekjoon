import sys
from collections import deque

n,Q=map(int,sys.stdin.readline().split())
graph=[[] for i in range(n+1)]
# graph[x]=(y,r) --> x에서 y의 usado=r

for i in range(n-1):
    p,q,r=map(int,sys.stdin.readline().split())
    graph[p].append((q,r))
    graph[q].append((p,r))

for i in range(Q):
    k,v=map(int,sys.stdin.readline().split())
    visit=[False]*(n+1)
    count=0
    queue=deque()
    queue.append((v,99999999999))
    visit[v]=True
    while queue:
        v,usado=queue.popleft()
        for v2,usado2 in graph[v]:
            usado2=min(usado,usado2)
            if usado2>=k and not(visit[v2]):
                queue.append((v2,usado2))
                count+=1
                visit[v2]=True
    print(count)
    