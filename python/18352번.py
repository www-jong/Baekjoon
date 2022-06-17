from collections import deque
import sys
n,m,k,x=map(int,sys.stdin.readline().split())
graph=[[] for i in range(1+n)]
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)

visit=[-1]*(n+1)
q=deque()
q.append(x)
visit[x]=0
ans=[]
while q:
    s=q.popleft()
    for i in graph[s]:
        if visit[i]==-1:
            visit[i]=visit[s]+1
            if visit[i]==k:
                ans.append(i)
            q.append(i)
ans.sort()
if len(ans)==0:
    print(-1)
else:
    print(*ans,sep="\n")