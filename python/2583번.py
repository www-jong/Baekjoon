from collections import deque

m,n,k=map(int,input().split())
dx=[0,0,1,-1]
dy=[1,-1,0,0]
graph=[[0]*(n+1) for i in range(m+1)]
visit=[[0]*(n+1) for i in range(m+1)]
count=0
ssa=[]

for i in range(k):
    x1,y1,x2,y2=map(int,input().split())
    for a in range(x1+1,x2+1):
        for b in range(y1+1,y2+1):
            graph[b][a]=1

for i in range(m+1):
    print(graph[i])

for a in range(1,m+1):
    for b in range(1,n+1):
        if graph[a][b]==1:
            continue
        q=deque()
        ddd=1
        count+=1
        q.append((a,b))
        graph[a][b]=1
        while q:
            x,y=q.popleft()
            for i in range(4):
                sx=x+dx[i]
                sy=y+dy[i]
                if 1<=sx<=m and 1<=sy<=n:
                    if graph[sx][sy]!=1:
                        q.append((sx,sy))
                        graph[sx][sy]=1
                        ddd+=1
        ssa.append(ddd)
print(count)
print(*sorted(ssa),sep=" ")
