from collections import deque
n,m=map(int,input().split())

ind=[0]*(n+1)
graph=[[] for i in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    ind[b]+=1
    
def topology_sort():
    res=[]
    q=deque()
    for i in range(1,n+1):
        #진입차수가 0이면
        if ind[i]==0:
            q.append(i)
    while q:
        cur=q.popleft()
        res.append(cur)
        for i in graph[cur]:
            ind[i]-=1
            if ind[i]==0:
                q.append(i)
    for i in res:
        print(i,end=' ')
topology_sort()